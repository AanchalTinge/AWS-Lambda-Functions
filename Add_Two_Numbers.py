import json

def lambda_handler(event, context):
    try:
        num1 = event.get("num1", 0)
        num2 = event.get("num2", 0)
        result = num1 + num2
        
        return {
            "statusCode": 200,
            "body": json.dumps({"sum": result})
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    ```
```json
{
    "num1": 5,
    "num2": 7
}
