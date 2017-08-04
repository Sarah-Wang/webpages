#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
import os
import Cookie

print "Content-type: text/html"
print

print """
<html>
<head>
<meta charset="utf-8">
<title>cookie get test</title>
</head>
<body>
<h1>读取cookie信息</h1>
"""

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['name'].value
        print "cookie data: "+data+"<br>"
    except KeyError:
        print "cookie not set or out of time<br>"
print """
</body>
</html>

"""