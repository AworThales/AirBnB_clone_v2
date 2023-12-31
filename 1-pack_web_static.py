#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:21:54 2020
@author: Robinson Montes
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['35.227.35.75', '100.24.37.33']


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    date_now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    directory = './versions/web_static_{}'.format(date_now)
    local('sudo tar -czvf {}.tgz web_static'.format(directory))
    name = '{}.tgz'.format(directory)
    if name:
        return name
    else:
        return None
