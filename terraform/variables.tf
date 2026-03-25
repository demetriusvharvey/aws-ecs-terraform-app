variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "cloud-engineer-project"
}

variable "container_port" {
  description = "Port the app listens on"
  type        = number
  default     = 5000
}