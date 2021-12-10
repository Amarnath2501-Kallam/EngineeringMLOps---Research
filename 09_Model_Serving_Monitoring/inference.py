import requests
import json
import os
import ssl
import pandas as pd

 

def allowSelfSignedHttps(allowed):

# bypass the server certificate verification on client side

    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):

        ssl._create_default_https_context = ssl._create_unverified_context

 

    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

 

# Request data goes here

 

data = pd.read_csv('validation_data.csv')

# you need to drop 4 columns for this to work.

data = data.drop(columns=['Timestamp', 'Location', 'Future_weather_condition', 'Pressure_millibars'])

 

url = ''

api_key = '' # Replace this with the API key for the web service

headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

 

for i in range(len(data)):

    inference_data = data.values[i].tolist()

    inference_data = json.dumps({"data": [inference_data]})

    inference_data = str.encode(inference_data)

 

    try:

        response = requests.request("POST", url, headers=headers, data=inference_data)

        result = response.text

        print(result)

    except requests.HTTPError as error:

        print("The request failed with status code: " + str(error.code))

 

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure

        print(error.info())

        print(json.loads(error.read().decode("utf8", 'ignore')))
