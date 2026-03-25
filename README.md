# aws-ecs-terraform-app# AWS ECS Fargate App with Terraform

## Project Overview

This project demonstrates how to deploy a containerized Python web application to AWS using Terraform, Docker, Amazon ECR, Amazon ECS Fargate, and an Application Load Balancer.

The goal of this project was to build a production-style cloud deployment that reflects real cloud engineering work, including infrastructure as code, containerization, networking, and application deployment.

## Architecture

Traffic flow:

Internet -> Application Load Balancer -> ECS Fargate Service -> Docker Container (stored in ECR)

AWS resources used:
- VPC
- Public Subnets
- Internet Gateway
- Route Tables
- Security Groups
- Amazon ECR
- Amazon ECS Fargate
- Application Load Balancer
- CloudWatch Log Group
- IAM Role for ECS Task Execution

## Tech Stack

- AWS
- Terraform
- Docker
- Python
- Flask
- Amazon ECR
- Amazon ECS Fargate
- Application Load Balancer
- CloudWatch

Application Endpoints
/ - Main application page
/health - Health check endpoint for the load balancer
What This Project Does
Builds a Docker image for a Python Flask app
Stores the image in Amazon ECR
Provisions AWS infrastructure using Terraform
Deploys the container to Amazon ECS Fargate
Exposes the app publicly through an Application Load Balancer
Uses CloudWatch for container logs
Uses a health check endpoint for availability monitoring

Deployment Steps:
1. Build the Docker image locally
docker build -t cloud-engineer-app .
2. Authenticate Docker to Amazon ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
3. Tag the image
docker tag cloud-engineer-app:latest <ecr-repository-url>:latest
4. Push the image to ECR
docker push <ecr-repository-url>:latest
5. Initialize Terraform
terraform init
6. Validate Terraform configuration
terraform fmt
terraform validate
7. Preview infrastructure changes
terraform plan
8. Deploy infrastructure
terraform apply
9. Force ECS service redeployment if needed
aws ecs update-service --cluster cloud-engineer-project-cluster --service cloud-engineer-project-service --force-new-deployment --region us-east-1

Skills Demonstrated:
Infrastructure as Code with Terraform
AWS networking and security design
Containerization with Docker
Container registry usage with Amazon ECR
Container orchestration with Amazon ECS Fargate
Load balancing with ALB
Health checks and application availability
Cloud logging with CloudWatch
End-to-end cloud application deployment

Key Learnings:
How to package an application into a Docker container
How to store and manage images in Amazon ECR
How ECS Fargate runs containers without managing EC2 servers
How an Application Load Balancer routes traffic to containers
How Terraform can provision repeatable AWS infrastructure
How cloud services connect together in a real deployment workflow

Future Improvements:
Add GitHub Actions CI/CD pipeline
Add Amazon RDS for a true 3-tier architecture
Add HTTPS with ACM and Route 53
Add CloudWatch alarms and dashboards
Add private subnets and NAT Gateway for stricter security
Add autoscaling for ECS service

## Architecture (3-Tier)

Internet → ALB → ECS Fargate → RDS PostgreSQL

- ALB handles incoming traffic
- ECS runs the containerized app
- RDS stores application data in private subnets****
