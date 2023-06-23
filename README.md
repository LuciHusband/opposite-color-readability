# Text Color Recommendation API

The Text Color Recommendation API is a service that suggests the optimal text color based on the background color provided. It helps frontend developers enhance the readability of text in their user interfaces, particularly when dealing with transparent elements or dynamically changing backgrounds.

## How to Use the API

The API provides a single endpoint for making a POST request to obtain the recommended text color.

### Endpoint

POST /changeTextColor

### Request Format

The request should be made with a JSON payload containing the background color.

Example request payload:

```json
{
  "backgroundColor": "#ff6956"
}
```

## Example Usaage

example usage is shown in file named "test.py"
