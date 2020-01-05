
from app import app
import pytest
from flask import json


class TestClass(object):
    def setup_class(self):
        app.config['TESTING'] = True  
        self.app = app.test_client()

    def teardown_class(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_get_all(self):
        response = self.app.get('/')
        data = response.get_data(as_text=True)
        assert response.status_code == 200

