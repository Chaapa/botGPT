import json

import requests

from config import TOKEN, CHATGPT_KEY

# OpenAI секретный ключ
API_KEY = CHATGPT_KEY
# Models: text-davinci-003,text-curie-001,text-babbage-001,text-ada-001
MODEL = 'text-davinci-003'

# Telegram токен бота
BOT_TOKEN = TOKEN
# определяем характер телеграм бота
BOT_PERSONALITY = '"I want you to act as a marketer. "'


# 2a. получаем ответ от OpenAI
def openAI(prompt):
    # запрос на OpenAI API
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={'model': MODEL, 'prompt': prompt, 'temperature': 0.5, 'max_tokens': 1000}
    )

    result = response.json()
    final_result = ''.join(choice['text'] for choice in result['choices'])
    return final_result


# 2b. функци получения изображения от OpenAI
def openAImage(prompt):
    # запрос на  OpenAI API
    resp = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={'prompt': prompt, 'n': 1, 'size': '1024x1024'}
    )
    response_text = json.loads(resp.text)

    return response_text['data'][0]['url']
