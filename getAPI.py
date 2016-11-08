#!/usr/bin/env python
import json
import numpy as np
import requests

respon = requests.get("http://agungdp.agri.web.id:3456/api/sensor")
hasil = json.loads(respon.text)

array_sensor = []
array_idSens = []
for val in hasil['data']:
	array_sensor.append(val['nilai_sensor'])
	array_idSens.append(val['id_sensor'])
print array_sensor
print array_idSens

jum = 0
for i in range(np.size(array_sensor)):
	jum += array_sensor[i]
print jum

print array_sensor[0]