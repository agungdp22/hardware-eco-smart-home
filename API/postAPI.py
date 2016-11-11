#!/usr/bin/env python
import urllib2
import datetime

# postData = 'curl -X POST -d "{\"nama_perangkat\": \"coba1\", \"pemakaian_daya\": \"10\"}" -H "Content-Type: application/json" http://localhost:3000/api/sensor'

class postAPI(object):
	def __init__(self, header):
		self.header = header

	def sensor(self,datetime,idSensor,nilai):
		data = '{"datetime":"'+str(datetime)+'","id_sensor": "'+str(idSensor)+'","nilai_sensor":"'+str(nilai)+'","header":"'+str(self.header)+'"}'
		url = 'http://agungdp.agri.web.id:3456/api/sensor'
		req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
		f = urllib2.urlopen(req)
		for x in f:
		    print(x)
		f.close()

	def fuzzy(self,datetime,varFuzzy):
		data = '{"datetime":"'+str(datetime)+'","fuzzy_rendah": "'+str(varFuzzy[0])+'","fuzzy_sedang":"'+str(varFuzzy[1])+'","fuzzy_tinggi":"'+str(varFuzzy[2])+'","header":"'+str(self.header)+'"}'
		url = 'http://agungdp.agri.web.id:3456/api/fuzzy'
		req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
		f = urllib2.urlopen(req)
		for x in f:
		    print(x)
		f.close()
