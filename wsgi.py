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
    documents = parse_htdocs_directory(working_directory, htdocs_dir)

    if os.path.split(environ['PATH_INFO'])[1] in documents.keys():
        full_path = "".join([working_directory, htdocs_dir, "/", documents[os.path.split(environ['PATH_INFO'])[1]][1]])
        return_value = read_file(full_path)
        start_response('200 OK', [('Content-Type', guess_mimetype(full_path))])
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
    for file_name in os.listdir(htdocs_path):
        file_path = "".join([htdocs_path, "/", file_name])
        if isfile(file_path):
            htdocs_files[os.path.splitext(file_name)[0]] = (file_path, file_name)
    return htdocs_files






