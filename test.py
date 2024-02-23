import requests

if __name__ == "__main__":
    local_service_url = "http://127.0.0.1:6003/api/queue"
    order = [
            {
                "strategy_no": "1001",
                "code": "513030",
                "name": "德国30",
                "ct_amount": 100,
                "operate": "buy"
                },
            {
                "strategy_no": "1001",
                "code": "162411",
                "name": "华宝油气",
                "ct_amount": 100,
                "operate": "sell"
            }
        ]
    try:
        response = requests.post(url=local_service_url,
                                 json=order)
        print(response.text)
    except Exception as e:
        print(e)