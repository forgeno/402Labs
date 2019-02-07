#!/usr/bin/env python3
import cgi
import cgitb
import json
import os
from urllib.parse import parse_qs

print("Content-Type: text/html\n")
print("<!doctype html>")
print("<head>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
cgitb.enable()

#Print query string
qs = os.environ.get("QUERY_STRING", None)
print("<dl>")
print("<dt>QUERY_STRING</dt>")
print("<dd>{}</dd>".format(parse_qs(qs)))
ua = os.environ.get("HTTP_USER_AGENT", None)
print("<dt>HTTP_USER_AGENT</dt>")
print("<dd>{}</dd>".format(ua))
print("</dl>")




print("<pre>")
print(json.dumps(dict((os.environ))))
print("</pre>")