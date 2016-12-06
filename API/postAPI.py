#!/usr/bin/env python
import urllib2
import time
import requests

# postData = 'curl -X POST -d "{\"nama_perangkat\": \"coba1\", \"pemakaian_daya\": \"10\"}" -H "Content-Type: application/json" http://localhost:3000/api/sensor'

class postAPI(object):
	def __init__(self, headerAPI):
		self.headers = headerAPI
		self.host = "http://agungdp.agri.web.id:2016"

	def putBaterai(self,persentase):
		data = '{"datetime":"'+str(self.datetime)+'","id_user": "1","id_rumah":"1","kapasitas":"'+str(persentase)+'"}'
		# url = 'http://agungdp.agri.web.id:2016/battery'
		url = 'http://10.42.0.1:2016/battery'
		response = requests.put(url, data, headers=self.headers)
		print(response.text)

	def postBaterai(self,persentase):
		data = '{"datetime":"'+str(self.datetime)+'","id_user": "1","id_rumah":"1","kapasitas":"'+str(persentase)+'"}'
		# url = 'http://agungdp.agri.web.id:2016/battery'
		url = self.host+'/battery'
		response = requests.post(url, data, headers=self.headers)
		print(response.text)

	def safeMode(self):
		datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
		data = '{"datetime":"'+str(datetime)+'","id_user": "1","status_safe":"1"}'
		url = self.host+'/safe'
		response = requests.post(url, data, headers=self.headers)
		print(response.text)

	def postDaya(self,daya):
		datetime = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
		data = '{"datetime":"'+str(datetime)+'","id_perangkat": "22","id_user": "1","id_rumah":"1","pemakaian_daya":"'+str(daya)+'"}'
		url = self.host+'/data'
		response = requests.post(url, data, headers=self.headers)
		print(response.text)