# AWS Serverless Directory: Elevated Care

## Why I Built This
I wanted to build a serverless healthcare directory with a security-first mindset from day one, 
proving I could enforce least privilege even on a project where the main visible output is just 
a clean frontend.

## What I Built
- **Frontend:** Responsive HTML5/CSS3 UI, hosted on Amazon S3.
- **API Layer:** Amazon API Gateway (REST) as a secure proxy between frontend and backend logic.
- **Compute:** AWS Lambda (Python) handling business logic and database queries on-demand.
- **Database:** Amazon DynamoDB for high-availability clinic listing storage.

## Security Focus: IAM Least Privilege
Instead of a broad administrative role, I scoped the Lambda's execution role to exactly 
`DynamoDBReadOnlyAccess`. Even if someone injected malicious code through the frontend, the 
backend is physically incapable of deleting or modifying database records.

## Challenges & Troubleshooting
- **CORS Policy Resolution:** Connecting the S3 frontend to API Gateway triggered CORS blocks. 
  I resolved it by enabling CORS headers in the API Gateway resource settings and manually 
  injecting `Access-Control-Allow-Origin` into the Lambda's Python response dictionary.
- **Lambda Proxy Integration Response:** Hit a 502 Bad Gateway until I restructured the Lambda's 
  return object to match AWS's strict proxy integration format: `statusCode`, `headers`, and a 
  JSON-stringified `body`.

## What I'd Do Next
This proves the least-privilege pattern, but I wouldn't call it production-ready. Next: Cognito 
user pools in front of the API, since a real healthcare directory can't sit on an open, 
unauthenticated endpoint even read-only; request validation models in API Gateway instead of 
trusting Lambda to catch bad input; and structured CloudWatch logging so every read is traceable 
to a specific request.
