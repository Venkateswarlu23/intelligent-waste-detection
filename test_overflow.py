from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="94lIFc6yIzpCf2HwBOgQ"
)

result = CLIENT.infer(
    "test.jpg",
    model_id="garbage-overflowing/1"
)

print(result)