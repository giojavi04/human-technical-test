from flask_restx import Namespace, fields


class CurrencyDto:
    api = Namespace('currency', description='currency related operations')
    currency = api.model('currency', {
        'public_id': fields.String(required=True, description='currency public_id'),
        'amount': fields.String(required=True, description='currency amount query'),
        'currency_from': fields.String(required=True, description='currency from'),
        'currency_to': fields.String(required=True, description='currency to'),
        'days': fields.String(description='currency latest five days'),
        'registered_on': fields.String(description='currency date of query'),
    })
