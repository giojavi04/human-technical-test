import uuid
import datetime
import requests
import json

from app.main import db
from app.main.model.currency import Currency
from app.main.util.converter import get_converted_currency

options = {
    '1': {
        'from': 'EUR',
        'to': 'USD'
    },
    '2': {
        'from': 'CLP',
        'to': 'USD'
    },
    '3': {
        'from': 'PEN',
        'to': 'USD'
    }
}

url_webhook = 'https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9'
# url_webhook = 'https://webhook.site/d61e7bbd-273f-41a5-899d-500871214bf9'


def save_amount(amount, option=1):
    get_data = get_converted_currency(amount, options[option]['from'], options[option]['to'], 5)

    new_currency = Currency(
        public_id=str(uuid.uuid4()),
        amount=amount,
        currency_from=options[option]['from'],
        currency_to=options[option]['to'],
        days=get_data,
        registered_on=datetime.datetime.utcnow()
    )
    save_changes(new_currency)
    return new_currency


def get_a_amount(amount_id):
    return Currency.query.filter_by(amount=amount_id).first()


def send_to_webhook(payload):
    return requests.post(url_webhook, {'amount': payload.amount, 'from': payload.currency_from,
                                       'to': payload.currency_to, 'days': payload.days})


def save_changes(data: Currency) -> None:
    db.session.add(data)
    db.session.commit()

