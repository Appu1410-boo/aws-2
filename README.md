# aws-2
1)Create a Lambda Function:
Log in to the AWS Management Console.
Navigate to the Lambda service and create a new function.
Choose "Author from scratch."
Select the runtime (e.g., Python 3.x).
2)Add the Code:
Paste the code above into the inline code editor.
Environment Variables (Optional):
Add the S3 bucket name as an environment variable for better configurability.
3)Test Event:
Create a test event with the following structure:                                                             {
  "file_name": "example.pdf",
  "file_content": "Base64EncodedFileContentHere"
}                                                                                                                       4)Replace "Base64EncodedFileContentHere" with actual Base64-encoded content of a PDF or document.                               To generate Base64-encoded content for testing:
base64 example.pdf > encoded_file.txt
5)Test the Function:
Run the test, and verify the file is uploaded to the specified S3 bucket.
