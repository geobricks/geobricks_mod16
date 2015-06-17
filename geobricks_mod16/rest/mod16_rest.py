import json
from flask import Blueprint
from flask import Response
from flask.ext.cors import cross_origin
from geobricks_mod16.core import mod16_core as m
from geobricks_mod16.resources.schemas.mod16_schema import schema


mod16 = Blueprint('modis', __name__)


@mod16.route('/discovery/')
@cross_origin(origins='*', headers=['Content-Type'])
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    return Response(json.dumps(schema), content_type='application/json; charset=utf-8')

@mod16.route('/<product_type>/')
@cross_origin(origins='*', headers=['Content-Type'])
def list_layers(product_type):
    """
    List all the available layers for the given product type.
    @param product_type: 'ET' or 'PET'.
    @type product_type: str
    @return: List of code/label objects.
    """
    out = m.list_layers(product_type)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')