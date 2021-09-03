from flask_restx import Api
from flask import Blueprint

from .main.controller.currency_controller import api as currency_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='HUMAN BRAND - TECHNICAL TEST',
    version='1.0',
    description='A simple api to technical test web service',
)

api.add_namespace(currency_ns, path='/currency')
