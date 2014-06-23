#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'edwin'
from wsgiref import simple_server
import wsgi
import os

httpd = simple_server.WSGIServer(('localhost', 8888), simple_server.WSGIRequestHandler)
httpd.set_app(wsgi.application)
httpd.serve_forever()