import pytest
import requests
from app.config import app


def test_get_all_produc():
    response = requests.get('http://localhost:5000/api/product')
    assert response.status_code == 200
    
def test_get_produc_by_code():
    response = requests.get('http://localhost:5000/api/product/123')
    assert response.status_code == 200
    
def test_get_all_produc_entry():
    response = requests.get('http://localhost:5000/api/product/entry')
    assert response.status_code == 200
    
def test_get_all_produc_out():
    response = requests.get('http://localhost:5000/api/product/output')
    assert response.status_code == 200
    
def get_all_user():
    response = requests.get('http://localhost:5000/api/user')
    assert response.status_code == 200
    
def test_item_output():
    response = requests.get('http://localhost:5000/api/item/output')
    assert response.status_code == 200
    
def test_item_entry():
    response = requests.get('http://localhost:5000/api/item/entry')
    assert response.status_code == 200