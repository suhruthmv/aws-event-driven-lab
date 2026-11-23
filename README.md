# AWS Event-Driven Architecture Lab ☁️

A hands-on project exploring serverless and event-driven architecture using Amazon Web Services.

## 🎯 Project Overview

Build a serverless task-processing pipeline that receives requests through an API, queues them for asynchronous processing, stores the results, and publishes completion notifications.

The goal is to demonstrate practical AWS architecture patterns with security, reliability, observability, and cost efficiency in mind.

## 🏗️ Planned Architecture

API Gateway → Lambda → SQS → Lambda → DynamoDB + SNS

Future enhancement: AWS Step Functions for multi-step workflow orchestration.

## 🛠️ Technology Stack

- **Language:** Python
- **Compute:** AWS Lambda
- **API:** Amazon API Gateway
- **Messaging:** Amazon SQS, Amazon SNS
- **Workflow:** AWS Step Functions (planned)
- **Database:** Amazon DynamoDB
- **Infrastructure as Code:** AWS CloudFormation
- **Monitoring:** Amazon CloudWatch
- **Security:** AWS IAM

## ✨ Planned Features

- REST API to submit tasks
- Asynchronous processing using SQS
- Task status and result tracking in DynamoDB
- Event notifications using SNS
- Retry handling and dead-letter queues
- Multi-step orchestration using Step Functions
- CloudWatch logging and monitoring
- Infrastructure deployment using CloudFormation

## 🚀 Development Roadmap

- [x] Initialize GitHub repository
- [ ] Design infrastructure and project structure
- [ ] Implement API Lambda
- [ ] Configure SQS and worker Lambda
- [ ] Integrate DynamoDB
- [ ] Add SNS notifications
- [ ] Implement error handling and monitoring
- [ ] Add Step Functions workflow
- [ ] Write tests and deployment instructions

## 📌 Project Status

Planning and initial development.

## 📄 License

MIT License
