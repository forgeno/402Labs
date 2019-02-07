#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
import os

form = cgi.FieldStorage()
f_username = form.getfirst("username","")
f_password = form.getfirst("password","")
c_username = None
cpassword = None
request_type = os.environ.get("REQUEST_METHOD","GET")
cookie_string = os.environ.get("HTTP_COOKIE")

cookies_split = cookie_string.split("; ")
if(cookies_split != None):
    for cookie_kv in cookies_split:
        k, v = cookie_kv.split("=")
        if(k =="username"):
            c_username = v
        if(k == "password"):
            c_password = v

    
#render the login form
print("Content-Type: text/html")

if(c_username and c_password):
    print()
    print(secret_page(f_username, f_password))

elif(request_type == "POST"):
    if(f_username == username and f_password == password):
        print("Set-Cookie: username={}".format(f_username))
        print("Set-Cookie: password={}".format(f_password))
        #LOGIN OKAY, SET COOKIE
        print()
        print(secret_page(f_username, f_password))
    else:
        print()
        print(after_login_incorrect())
else:
    print()
    print(login_page())
    print(cookie_string)
#print(username,password)