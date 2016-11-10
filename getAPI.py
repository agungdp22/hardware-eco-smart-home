#!/usr/bin/env python
import json
import numpy as np
import requests
from fuzzy.fuzzy import fuzzy

respon = requests.get("http://agungdp.agri.web.id:3456/api/sensor")
hasil = json.loads(respon.text)

# membership function variabel cahaya
cahayarendah = [0,80,160] # trapezoid
cahayasedang = [100,150,200] # segitiga
cahayatinggi = [155,220] # trapezoid

# membership function variabel baterai
bateraisedikit = [0,1,3]
bateraisedang = [2,4,6]
bateraibanyak = [5,7]


array_sensor = []
array_idSens = []
for val in hasil['data']:
	array_sensor.append(val['nilai_sensor'])
	array_idSens.append(val['id_sensor'])
# print array_sensor
# print array_idSens

print "Nilai LDR:",array_sensor[0], ", Sensor ke-",array_idSens[0]

initFuzzy = fuzzy(array_sensor[0],array_idSens[0],1)
initFuzzy.membershipCahaya(cahayarendah,cahayasedang,cahayatinggi)
initFuzzy.membershipBaterai(bateraisedikit,bateraisedang,bateraibanyak)

getFuzCah = initFuzzy.fuzzifikasiCahaya()
getFuzBat = initFuzzy.fuzzifikasiBaterai()
getMin = initFuzzy.getMinimal()

print "Nilai Fuzzifikasi Cahaya: ",getFuzCah
print "Nilai Fuzzifikasi Sensor: ",getFuzBat
print "Nilai Minimal Tiap Rule : ",getMin