import requests


def currency_converter(from_currency, to_currency, value):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['rates'][to_currency]
        converted_value = value * exchange_rate
        return {'from': from_currency, 'to': to_currency, 'value': value, 'converted_value': converted_value}

    else:
        return {'error': 'Failed to fetch exchange rates'}


# Пример запроса
print('ВВедите сокращение валюты которую хотите перевести на ангийском')
from_currency = str(input())
print('ВВедите сокращение валюты в которую хотите перевести на ангийском')
to_currency = str(input())
print('Введите количесво исходной валюты')
value = float(input())

response = currency_converter(from_currency, to_currency, value)
print(response)
