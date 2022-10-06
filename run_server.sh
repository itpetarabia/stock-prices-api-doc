#!/bin/bash
export FLASK_APP=server.py 
export FLASK_ENV=development
python3 -m flask run -p 5000
