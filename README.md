# AWS Serverless Directory: Elevated Care

## 🚀 Project Overview
A serverless, high-end healthcare waitlist and directory application built to demonstrate secure cloud architecture. The system features a modern **Glassmorphism UI** and an event-driven backend that fetches real-time clinic data from a NoSQL database.

## 🏗️ Architecture
- **Frontend:** Responsive HTML5/CSS3 UI with an "Elevated Care" aesthetic, hosted on **Amazon S3**.
- **API Management:** **Amazon API Gateway** (REST API) acting as a secure proxy between the frontend and backend logic.
- **Compute:** **AWS Lambda (Python)** executing business logic and database queries on-demand.
- **Database:** **Amazon DynamoDB** utilized for high-availability storage of clinic listings.

## 🔒 Security focus: IAM Least Privilege
As an aspiring Cybersecurity specialist, I built this project with a **"Security First"** mindset. 
* **Scoped Permissions:** Instead of using broad administrative roles, I configured a custom execution role for the Lambda function.
* **Policy Enforcement:** The function is restricted to **`DynamoDBReadOnlyAccess`**. This ensures that even if a malicious actor attempted to inject code into the frontend, they would be physically unable to delete or modify the database records via the backend.

## 🛠️ Challenges & Troubleshooting
### 1. CORS Policy Resolution
While connecting the S3 frontend to the API Gateway, I encountered **Cross-Origin Resource Sharing (CORS)** blocks. I resolved this by:
- Enabling CORS headers in the API Gateway Resource settings.
- Manually injecting `Access-Control-Allow-Origin` headers into the Lambda Python response dictionary to satisfy browser security requirements.

### 2. Lambda Proxy Integration Response
I overcame a **502 Bad Gateway** error by restructuring the Lambda return object to follow the strict AWS Proxy Integration format, ensuring the `statusCode`, `headers`, and `body` (JSON stringified) were perfectly aligned.
