import requests
import json

def yandex_ai(message):

    url ="https://llm.api.cloud.yandex.net/llm/v1alpha/chat"
    data={
        "modelUri": "gpt://ajeaokr05g96num95usd/yandexgpt-lite",
        "model":"general",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "1000"
        },
        "messages": [
            {
            "role": "system",
            "text": f"{message}"
            },
  ]
    }
    headers={
        "Authorization": f'Api-Key {"AQVN11Z1iRGCNNRKpNy1ltaMfDG5vPEPrkiX3LRY"}',
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
      print(response.text)
      data_dict = response.json()
      data = data_dict['result']['message']['text']
      return data
    else:
      return False