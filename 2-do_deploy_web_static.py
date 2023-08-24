#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:21:54 2020
@author: Robinson Montes
"""
from fabric.api import local, put, run, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['35.227.35.75', '100.24.37.33']

def do_pack():
    """
    Targginng project directory into a packages as .tgz
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

def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        directory = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(directory))
        run('tar -xzf /tmp/{} -C {}'.format(archive, directory))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(directory, directory))
        run('rm -rf {}/web_static'.format(directory))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(directory, current))
        print('New version deployed!')
        return True
    except:
        return False
