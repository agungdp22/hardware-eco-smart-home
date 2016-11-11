#!/usr/bin/env python
import json
import numpy as np
import requests

class getAPI(object):
	def __init__(self, header):
		self.header = header

	def sensor(self):
		respon = requests.get("http://agungdp.agri.web.id:3456/api/sensor")
		hasil = json.loads(respon.text)
		array_sensor = []
		array_idSens = []
		for val in hasil['data']:
			array_sensor.append(val['nilai_sensor'])
			array_idSens.append(val['id_sensor'])
		return array_sensor