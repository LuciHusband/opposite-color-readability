import requests

# API endpoint URL
url = 'http://localhost:5000/changeTextColor'

# Request payload
payload = {
    'backgroundColor': '#ff6956' # Change this to test different colors
}

# Make the POST request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Successful request
    data = response.json()
    text_color = data['textColor']
    print(f"Recommended text color: {text_color}")
else:
    # Error occurred
    print(f"Error: {response.status_code} - {response.text}")
