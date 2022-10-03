
import requests

header = {"some_header":"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=header)

print(response.text)# какие заголовки пришди на сервер
print(response.headers) #какие заголовки пришли клиенту на запрос