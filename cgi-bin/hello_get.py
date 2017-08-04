#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename：hello_get.py
# usage example: localhost/cgi-bin/hello_get.py?name=namefromURL&url=http://www.do.not.tell.you.com


# CGI处理模块
import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2>%s： %s</h2>" % (site_name, site_url)
print "</body>"
print "</html>"