# Text Color Recommendation API

The Text Color Recommendation API is a service that suggests the optimal text color based on the background color provided. It helps frontend developers enhance the readability of text in their user interfaces, particularly when dealing with transparent elements or dynamically changing backgrounds.

![resim](https://github.com/LuciHusband/opposite-color-readability/assets/119350016/36ac8e83-980a-469f-b706-b170e343f6c3)

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
For that case recommended text color is #0096a9

## Example Usaage

example usage is shown in file named "test.py"
