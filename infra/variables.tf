variable "aws_region" {
  description = "AWS region to deploy resources into"
  type        = string
  default     = "us-east-2"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket to trigger the Lambda function"
  type        =  string
  default     = "hello-lambda-trigger-bucket-tjr" # IMPORTANT: Change this to a globally unique name
}
