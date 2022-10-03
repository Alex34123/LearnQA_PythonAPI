import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
print(response.text)