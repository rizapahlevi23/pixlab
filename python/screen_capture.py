import requests
import json

# Extarct a scrren capture from a given website
website = 'https://github.com'

req = requests.get('https://api.pixlab.io/screencapture',params={'url':website,'key':'My_PixLab_Key'}) # You can optionally, speciy the desired width & height also
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("The Website screen capture is located on: " + reply['link'])