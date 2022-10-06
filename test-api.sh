#!/bin/bash
# mapi run --header-auth "api_key: hola" stock-prices auto openapi.yaml --url 127.0.0.1:5000 --interactive
mapi run --header-auth "api_key: hola" stock-prices 2min openapi.yaml --url 127.0.0.1:5000 --interactive