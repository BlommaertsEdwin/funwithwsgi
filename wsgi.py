#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'edwin'
import os
import mimetypes
from os.path import isfile


def application(environ, start_response):

    working_directory = os.getcwd()
    htdocs_dir = "/htdocs"
    index_file = "/index.html"
    static_directory = "/static"
    path = environ.get('PATH_INFO')

    #TODO: refactor this method to use the parse method instead of hardcoded values
    if environ['PATH_INFO'] == '/about':
        file = "/about.html"
        full_path = "".join([working_directory, htdocs_dir, file])
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
        full_path = "".join([working_directory, htdocs_dir, index_file])
        return_value = read_file(full_path)
        start_response('200 OK', [('Content-Type', guess_mimetype("".join([path, index_file])))])
        print parse_htdocs_directory(working_directory, htdocs_dir)
        return [return_value]


def read_file(path):
    with open(path) as file:
        data = file.read()
    return data


def guess_mimetype(path):
    mimetypes.init()
    return mimetypes.guess_type(path)[0]

def parse_htdocs_directory(path, htdocs_dir):
    htdocs_files = {}
    htdocs_path = "".join([path, htdocs_dir])
    for file in os.listdir(htdocs_path):
        file_path = "".join([htdocs_path, "/", file])
        if isfile(file_path):
            htdocs_files[os.path.splitext(file)[0]] = file_path
    return htdocs_files






