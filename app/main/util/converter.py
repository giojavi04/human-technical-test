import requests
import datetime


def get_converted_currency(amount, currency, converted_currency, amount_days):
    # Set the start date
    today_date = datetime.datetime.now()
    date_days = (today_date - datetime.timedelta(days=1 * amount_days))

    # Requests
    url = 'https://api.exchangerate.host/timeseries'
    payload = {'base': currency, 'amount': amount, 'start_date': date_days.date(), 'end_date': today_date.date()}
    response = requests.get(url, params=payload)
    data = response.json()

    # Data
    currency_history = {}

    for item in data['rates']:
        current_date = item
        currency_rate = data['rates'][item][converted_currency]

        currency_history[current_date] = currency_rate

    return currency_history
