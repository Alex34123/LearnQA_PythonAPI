from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text) #выводим на экран текст полученный при запросе get на метод get_text

try:
    parsed_response_text = response.json() #парсим переменную response
    print(parsed_response_text) #выводим распарсеную переменную на экран
except JSONDecodeError:  #если ошибка такая то выводим на экран сообщение ниже
    print("Response is not a JSON format")


