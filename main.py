import requests


def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    params = {"apikey": api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["rates"].get(to_currency)
    else:
        print(
            f"Error: Unable to fetch exchange rate. Status code: {response.status_code}"
        )
        return None


def convert_currency_with_api(amount, from_currency, to_currency, api_key):
    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        result = (
            f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
        )
        return result
    else:
        return "Conversion failed."


# Example usage:
api_key = "your_exchange_rate_api_key"
amount_to_convert = float(input("Enter the amount to convert: "))
from_currency = input("Enter the source currency in ISO code: ")
to_currency = input("Enter the target currency in ISO code: ")

result = convert_currency_with_api(
    amount_to_convert, from_currency, to_currency, api_key
)
print(result)
