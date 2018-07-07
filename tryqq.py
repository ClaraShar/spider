#-*-coding:utf-8-*-
import urllib.request

response = urllib.request.urlopen("http://index.baidu.com/?tpl=trend&word=lng%B4%AC")
html=str(response.read(),'utf-8')
print(html)
