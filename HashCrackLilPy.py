#!/usr/bin/python

#coding By LIlPy-ON 



import requests
import sys
import re
url = 'https://hashtoolkit.com/reverse-hash?hash='
try:
	hasH = sys.argv[1]
except:
	print ("usage: python "+sys.argv[0]+" hash")
	sys.exit()
http = requests.get(url+hasH)
content = http.content
cracked = re.findall("<span title=\"decrypted(md5|sha1|sha256|sha384|sha512) hash\">(.*)</span>", content)
print ("\n\tAlgoritimo: "+cracked[0][0])
print ("\tPassword cracked: "+cracked[0][1])