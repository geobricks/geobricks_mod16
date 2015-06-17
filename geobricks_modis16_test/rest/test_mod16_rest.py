import json
import unittest
from flask import Flask
from geobricks_mod16.rest.mod16_rest import mod16


class GeobricksMod16RestTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(mod16, url_prefix='/mod16')
        self.tester = self.app.test_client(self)

    def test_discovery(self):
        response = self.tester.get('/mod16/discovery/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(out['title'], 'MOD16')
        self.assertEquals(out['properties']['service_type']['default'], 'DATASOURCE')

    def test_list_layers(self):
        response = self.tester.get('/mod16/ET/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(len(out), 180)
        response = self.tester.get('/mod16/PET/', content_type='application/json')
        out = json.loads(response.data)
        self.assertEquals(len(out), 180)