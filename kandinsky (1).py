import json
import time
import base64
import requests
class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024, style = 0):
        styles = ['KANDINSKY', 'UHD', 'ANIME', 'DEFAULT']
        params = {
        "type": "GENERATE",
        "numImages": images,
        "width": width,
        "height": height,
        "styles": styles[style],
        "generateParams": {
            "query": f"{prompt}"
            }
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            attempts -= 1
            time.sleep(delay)

def save_image(image_data, id):
    try:
        with open(f"{id}.jpg", "wb") as file:
            file.write(image_data)
            return id
    except:
        print('Файл не найден')
        return False

def kandinsky_ai(message, id):
    try:
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '433BA89D7003A825C59B0AFF11D9B7AD', '0991A6E6A3ABC3F3CF9A554BB5A8B541')
        model_id = api.get_model()
        uuid = api.generate(message, model_id)
        images = api.check_generation(uuid)
        image_base64 = images[0]
        image_data = base64.b64decode(image_base64)
        save_image(image_data, id)
        return (f'{id}.jpg')
    except:
        print('Запрос неверный')
        return False