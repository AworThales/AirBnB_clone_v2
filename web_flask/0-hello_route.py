#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:15:54 2023
@author: Thales Solomon
"""
from flask import Flask
my_app = Flask(__name__)

@my_app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
