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

	def perangkat(self):
		url = "http://agungdp.agri.web.id:3456/mobile/getAPI"
		respon = requests.get(url, headers=self.header)

		# print respon.json()
		# print respon.headers['content-type']

		if respon.status_code==422:
			return respon.json()['status']
		else:
			hasil = json.loads(respon.text)
			array_perangkat = []
			for val in hasil['data']:
				array_perangkat.append([val['nama_perangkat'],val['status']])
			return array_perangkat