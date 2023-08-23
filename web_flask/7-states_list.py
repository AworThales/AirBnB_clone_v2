#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:15:54 2023
@author: Thales Solomon
"""
from models import storage
from models.state import State
from flask import Flask, render_template
my_app = Flask(__name__)

@my_app.teardown_appcontext
def appcontext_teardown(self):
    """use storage for fetching data from the storage engine
    """
    storage.close()

@my_app.route('/states_list', strict_slashes=False)
def state_info():
    """Display a HTML page inside the tag BODY"""
    return render_template('7-states_list.html',
                           states=storage.all(State))

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
