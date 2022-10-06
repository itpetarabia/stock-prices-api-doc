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

@app.route('/product', methods=['POST'])
@require_auth
def getproduct():
  data = request.json
  if not isinstance(data, dict):
    return '', 400
  barcodes = data.get('barcodes')
  if not barcodes:
    return '',400
  if not isinstance(barcodes, Sequence):
    return '', 400
  if not all((isinstance(item, str) for item in barcodes)):
    return '', 400
  barcodes = set(barcodes) # to remove duplicate entries

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
      matched_products.append(prod)

  if not matched_products:
    return 'Not Found!', 404
  return jsonify(matched_products), 200

    

if __name__ == '__main__':
  app.run()
