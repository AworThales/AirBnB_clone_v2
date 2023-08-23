#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:15:54 2023
@author: Thales Solomon
"""
from flask import Flask
from flask import render_template
my_app = Flask(__name__)

@my_app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'

@my_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Adding a specific route /hbnb"""
    return 'HBNB'

@my_app.route('/c/<string:text>', strict_slashes=False)
def c_text(text=None):
    """Dynamic inputed text: C + replace _ for space and show text"""
    return "C {}".format(text.replace('_', ' '))

@my_app.route('/python', strict_slashes=False)
@my_app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """Dynamic inputed text: Python + replace _ for space and show text"""
    return "Python {}".format(text.replace('_', ' '))

@my_app.route('/number/<int:n>', strict_slashes=False)
def only_digits_dynamic(n=None):
    """Dynamic inputted integer"""
    return "{} is a number".format(n)

@my_app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@my_app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def conditional_templating(n=None):
    """Display a HTML page only if n is an integer odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
