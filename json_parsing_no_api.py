import json

string_as_json_format = '{"answer": "Hello, Alex"}' # задаем переменную в формате json
obj = json.loads(string_as_json_format) # парсим переменную исп, loads

key = "answer"
if key in obj:
    print(obj[key])  #обращаемся к ключу answer в словаре obj и возвращаем его значение
else:
    print(f"Ключа {key} нет в JSONe")
