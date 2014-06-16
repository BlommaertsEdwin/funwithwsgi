#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'edwin'
import os
import mimetypes


def application(environ, start_response):

    working_directory = os.getcwd()
    htdocs = "/htdocs"
    index_file = "/index.html"
    static_directory = "/static"
    path = environ.get('PATH_INFO')

    if environ['PATH_INFO'] == '/about':
        file = "/about.html"
        full_path = "".join([working_directory, htdocs, file])
        return_value = read_file(full_path)
        start_response('200 OK', [('Content-Type', guess_mimetype("".join([path, file])))])
        return [return_value]

    elif path.find("/favicon.ico") == 0:
        start_response('200 OK', [('Content-type', guess_mimetype(path))])
        return [open("".join([working_directory, static_directory, environ['PATH_INFO']])).read()]

    elif path.find(static_directory) == 0:
        start_response('200 OK', [('Content-type', guess_mimetype(path))])
        return [open("".join([working_directory, environ['PATH_INFO']])).read()]
    else:
        full_path = "".join([working_directory, htdocs, index_file])
        return_value = read_file(full_path)
        start_response('200 OK', [('Content-Type', guess_mimetype("".join([path, index_file])))])
        return [return_value]


def read_file(path):
    with open(path) as f:
        data = f.read()
    return data


def guess_mimetype(path):
    mimetypes.init()
    return mimetypes.guess_type(path)[0]







