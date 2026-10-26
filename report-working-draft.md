# CS79C AWS Architecture Portfolio Report — Working Draft

> Replace every bracketed item with your actual deployment/test results. Do not claim a test succeeded until you have observed it. Keep the final PDF between 3 and 5 pages, excluding diagrams/screenshots.

## 1. Executive summary
I built a serverless expense tracker API using Amazon API Gateway, AWS Lambda, Amazon DynamoDB, and Amazon CloudWatch. The API is designed to save expense records and return the stored records. CloudFormation defines the infrastructure so it can be recreated consistently.

**Observed deployment status:** [fill in]
**Observed POST result:** [fill in]
**Observed GET result:** [fill in]

## 2. Architecture and alternatives
Describe the request flow: client → API Gateway HTTP API → Python Lambda → DynamoDB. Lambda logs go to CloudWatch Logs, and a CloudWatch alarm monitors Lambda errors. CloudFormation creates the resources.

Alternatives considered: EC2 with a web server and database would require more server administration; a relational database could support more complex relationships but is unnecessary for this small key-value use case.

Insert the committed architecture diagram here.

## 3. Implementation, reproduction, challenges, and testing
List the deployment command and region. Include the real API URL output, POST and GET commands, and actual results. Describe any deployment or debugging problems you encountered and how you resolved them.

## 4. Security, reliability, performance, and cost
**Security:** Lambda uses an IAM role with only the DynamoDB actions needed by the application and CloudWatch logging permissions. The API is publicly reachable and has no user authentication, so it is a learning demo and should not be used for private financial data as-is.

**Reliability / disaster recovery:** API Gateway, Lambda, and DynamoDB are managed services. DynamoDB on-demand capacity avoids provisioning read/write capacity for this demo. A single-region deployment still has regional disaster-recovery limitations. State an appropriate recovery time objective (RTO) and recovery point objective (RPO) for this demo, and explain that cross-region recovery is not configured.

**Performance / scaling:** Lambda scales with incoming requests within service/account limits; DynamoDB uses on-demand capacity. A `Scan` operation becomes inefficient as the table grows, so production code should use query patterns and pagination.

**Cost estimate:** [add a real AWS Pricing Calculator estimate and its assumptions, such as region, expected request volume, stored data, and retention period.]

**Two cost optimizations:** 1) Keep the demo resources only while collecting evidence and delete the stack afterward. 2) Monitor actual usage and set a billing budget/alert; retain on-demand DynamoDB for low or unpredictable traffic rather than provisioning excess capacity.

## 5. AWS Well-Architected review: three pillars
**Security — strength:** scoped Lambda role for the required DynamoDB operations. **Improvement:** add authentication/authorization, input limits, and stronger protection before handling real user data.

**Reliability — strength:** managed API Gateway/Lambda/DynamoDB components and a CloudWatch error alarm. **Improvement:** add tested backups and a documented recovery procedure if the application becomes important.

**Cost Optimization — strength:** serverless compute and DynamoDB on-demand billing. **Improvement:** use a budget alert and review actual cost/usage; remove unused resources after the project.

## 6. What I would do differently
For a production version, I would add authentication, pagination and filtered queries, automated tests, backup/recovery testing, and deployment validation before exposing the API to users.
