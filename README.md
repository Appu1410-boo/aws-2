# aws-2
Create a Lambda Function:
Log in to the AWS Management Console.
Navigate to the Lambda service and create a new function.
Choose "Author from scratch."
Select the runtime (e.g., Python 3.x).
Add the Code:
Paste the code above into the inline code editor.
Environment Variables (Optional):
Add the S3 bucket name as an environment variable for better configurability.
Test Event:
Create a test event with the following structure: {
  "file_name": "example.pdf",
  "file_content": "Base64EncodedFileContentHere"
}
