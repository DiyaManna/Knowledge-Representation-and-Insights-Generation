import requests
import json

# Define the URL for the API endpoint
url = "http://127.0.0.1:5000/api/ask"

# Define the question you want to ask
question = "What is the average value of column_name?"

# Create the payload
data = {"question": question}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    print("Response from the API:")
    print(response.json())
else:
    print(f"Failed to get a response. Status code: {response.status_code}")
    print(response.text)