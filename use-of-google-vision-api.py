# Running the Vision API
from googleapiclient.discovery import build
import base64

APIKEY="REPLACE-API-KEY"  # Replace with your API key
IMAGE="path to you image"
vservice = build('vision', 'v1', developerKey=APIKEY)
request = vservice.images().annotate(body={
        'requests': [{
                'image': {
                    'source': {
                        'gcs_image_uri': IMAGE
                    }
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 3,
                }]
            }],
        })
responses = request.execute(num_retries=3)

# Let's output the `responses`
print(responses)
