
import json
import logging
import os
import uuid

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sqs = boto3.client("sqs")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    # Parse the incoming API request.
    try:
        body = event.get("body") or "{}"
        data = json.loads(body) if isinstance(body, str) else body
    except (TypeError, ValueError):
        return response(400, {"error": "Invalid JSON"})

    # Validate the message.
    if not isinstance(data, dict):
        return response(400, {"error": "Expected a JSON object"})

    message = data.get("message")

    if (
        not isinstance(message, str)
        or not 1 <= len(message.strip()) <= 500
    ):
        return response(400, {
            "error": "Message must contain 1-500 characters"
        })

    queue_url = os.environ.get("TASK_QUEUE_URL")

    if not queue_url:
        logger.error("TASK_QUEUE_URL is not configured")
        return response(500, {"error": "Service configuration error"})

    task_id = str(uuid.uuid4())

    task = {
        "task_id": task_id,
        "task_type": "echo",
        "payload": {"message": message.strip()},
    }

    # Send the task for asynchronous processing.
    try:
        sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(task),
        )
    except (BotoCoreError, ClientError):
        logger.exception("Failed to enqueue task")
        return response(502, {"error": "Unable to queue task"})

    return response(202, {
        "task_id": task_id,
        "status": "queued",
    })
