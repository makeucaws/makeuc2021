import boto3
import urllib
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # Get the object from the event and show its content type
    s3BucketName = event['Records'][0]['s3']['bucket']['name']
    documentName = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    # Amazon Textract client
    textract = boto3.client('textract')
    # Call Amazon Textract
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
            }
        })
    #print(response)
    # Print detected text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print ( item["Text"] )
