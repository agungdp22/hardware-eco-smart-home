#!/usr/bin/env python
import json
import numpy as np
import requests
import time

class getAPI(object):
	def __init__(self, header):
		self.header = header
		self.statusURL = "http://agungdp.agri.web.id:2016/status"

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
		respon = requests.get(self.statusURL, headers=self.header)
		# print(respon.text)
		hasil = json.loads(respon.text)
		array_perangkat = []
		for val in hasil:
			array_perangkat.append([val['id_perangkat'],val['status']])
		return array_perangkat

		# print respon.json()
		# print respon.headers['content-type']

		# if respon.status_code==422:
		# 	return respon.json()['status']
		# else:
		# 	hasil = json.loads(respon.text)
		# 	array_perangkat = []
		# 	for val in hasil['data']:
		# 		array_perangkat.append([val['nama_perangkat'],val['status']])
		# 	return array_perangkat

	def cekBuff(self):
		inDB = self.perangkat()
		time.sleep(1)
		respon = requests.get(self.statusURL, headers=self.header)
		hasil = json.loads(respon.text)
		inNOW = []
		for val in hasil:
			inNOW.append([val['id_perangkat'],val['status']])

		print inDB
		print inNOW
		if inNOW!=inDB:
			for cek in range(len(inDB)):
				if inNOW[cek]!=inDB[cek]:
					return inNOW[cek]
		else:
			return "berubah"
		# print inDB
		# print inNOW
		# return inDB!=inNOW