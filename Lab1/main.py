#!/usr/bin/env python

import requests

print(requests.__version__)
r = requests.get("https://raw.githubusercontent.com/forgeno/404Lab1/master/main.py")
print(r.text)
print(r.status_code)
