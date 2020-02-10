#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'simple_proxy_server',
        version = '1.0',
        install_requires = [
                'requests', 
                'git+https://github.com/constverum/ProxyBroker.git@master'], 
        description = 'simple proxy server',
        url = 'https://github.com/zhouxianggen/simple_proxy_server', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['simple_proxy_server'],
        data_files = [ ], 
        )

