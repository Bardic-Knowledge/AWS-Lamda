import os
import boto3
from PIL import Image, ImageDraw, ImageFont
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract the bucket and key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Load the image from S3
    image_obj = s3.get_object(Bucket=bucket, Key=key)
    image_data = image_obj['Body'].read()
    image = Image.open(io.BytesIO(image_data))

    # Create a drawing context to add the watermark
    draw = ImageDraw.Draw(image)
    
    # Define the watermark text, font, size, and position
    watermark_text = "dimaggio.dev"
    font = ImageFont.truetype("arial.ttf", 24)
    text_width, text_height = draw.textsize(watermark_text, font)
    position = ((image.width - text_width) // 2, image.height - text_height - 10)

    # Add the watermark to the image
    draw.text(position, watermark_text, (255, 255, 255), font=font)
    
    # Save the watermarked image
    output_buffer = io.BytesIO()
    image.save(output_buffer, format='JPEG')
    
    # Upload the watermarked image back to S3
    watermark_key = "wm_" + os.path.basename(key)
    s3.put_object(Bucket=bucket, Key=watermark_key, Body=output_buffer.getvalue())
    
    #return the new image name
    return {
        "statusCode": 200,
        "body": "Image watermarked and stored as " + watermark_key,
    }
