#! /usr/bin/env python3.6
# Python 3.6 or newer required.

import json
from typing import Sequence
import yaml
from flask import Flask, jsonify, render_template, make_response, request



app = Flask(__name__, static_folder='.',
            static_url_path='', template_folder='.')


def require_auth(func):
  def inner(*args, **kwargs):
    headers = request.headers
    api_key = headers.get('api_key', '')
    if api_key != 'hola':
        return '', 401
    return func(*args, **kwargs)
  inner.__name__ = func.__name__ # to avoid naming clashes
  return inner

@app.route('/branch', methods=['GET'])
@require_auth
def getbranches():
  branches = [ 
      {
      "id": 98,
      "name": "Budaiya"
      }
  ]
  return jsonify(branches), 200

@app.route('/allproducts', methods=['GET'])
@require_auth
def getproducts():
  products =[
    {
    "barcode": "99009910",
    "name": "Taste of the Wild",
    "price": 32.5,
    "quantities": [{
      "branch_id": 19,
      "quantity": 42
      }]
  }]
    
  return jsonify(products), 200

@app.route('/product', methods=['GET'])
@require_auth
def getproduct():
  barcodes = request.json
  if not isinstance(barcodes, Sequence):
    return 'Invalid Type Error', 400
  if not all((isinstance(item, str) for item in barcodes)):
    return 'Invalid Type Error', 400

  products =[
    {
    "barcode": "99009910",
    "name": "Taste of the Wild",
    "price": 32.5,
    "quantities": [{
      "branch_id": 19,
      "quantity": 42
      }]
    },
    {
    "barcode": "121009",
    "name": "Dog Collar",
    "price": 10.5,
    "quantities": [{
      "branch_id": 19,
      "quantity": 12
      }]
    }
  ]
  matched_products = []
  for prod in products:
    if prod['barcode'] in barcodes:
      matched_products.append(prod['barcode'])
  return jsonify(matched_products), 200

    

if __name__ == '__main__':
  app.run()
