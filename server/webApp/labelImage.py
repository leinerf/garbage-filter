import requests

def getImageLabel():
    url = "api url"
    # Adding empty header as parameters are being sent in payload
    headers = {
        "Prediction-Key": "secret_prediction_key",
        "Content-Type": "application/json"
    }
    data = {
        "Url": "https://s3-us-west-2.amazonaws.com/sbhacksv-garbage-collector/photo.jpg"
    }

    r = requests.post(url, json=data, headers=headers)
    data = r.json()["predictions"]
    return data

