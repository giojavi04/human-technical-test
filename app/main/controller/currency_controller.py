from flask import request
from flask_restx import Resource

from ..util.dto import CurrencyDto
from ..service.currency_service import save_amount, get_a_amount, send_to_webhook

api = CurrencyDto.api
_currency = CurrencyDto.currency


@api.route('/')
class CurrencyList(Resource):
    @api.doc('list_of_currencies_saved')
    @api.marshal_with(_currency, envelope='data')
    def get(self):
        """List all registered currencies"""
        amount = request.args.get('amount')
        option = request.args.get('option')
        if amount:
            return save_amount(amount, option)
        else:
            api.abort(401)


@api.route('/<amount>')
@api.param('amount', 'The Amount to query')
@api.response(404, 'Amount not found.')
class Currency(Resource):
    @api.doc('get a amount')
    @api.marshal_with(_currency)
    def get(self, amount):
        """get a currency given its amount"""
        currency = get_a_amount(amount)
        if not currency:
            api.abort(404)
        else:
            send_to_webhook(currency)
            return currency



