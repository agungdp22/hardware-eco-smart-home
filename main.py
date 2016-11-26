#!/usr/bin/env python
import time
import numpy as np
from I2C_Arduino.i2c import i2c
from API.getAPI import getAPI
from API.postAPI import postAPI
from anfis.trainingData import trainingData as tryAnfis

def kendali(getdata):
	hasil = getdata.perangkat()
	oper = []
	nilai = 0
	siz = np.size(hasil)/2 -1
	for i in hasil:
		oper.append(i[1])
		nilai += i[1]*(2**siz)
		siz-=1
	# kirim = hasil[0]*2 + hasil[1]
	konekArduino.kirimData(nilai)
	print oper
	# print nilai

def safemode(persentase, jumlahdaya):
	predik = anf.keputusan(persentase,jumlahdaya)
	return predik

# Training data dulu
anf = tryAnfis(epochs=10)
anf.training()
print "Training Data Selesai...."

# alamat i2c, disamain dgn yg di arduino->0x2a
address = 0x2a
headerAPI = {'Authorization': 'coegsekali ', "Content-Type": "application/json"}

postdata = postAPI(headerAPI)
getdata = getAPI(headerAPI)
konekArduino = i2c(address)
print "Device ready..."

while True:
	x=int(input("Persentase: "))
	y=int(input("Daya: "))
	postdata.postBaterai(x)
	isSafe = safemode(x,y)
	if isSafe:
		postdata.safeMode()
		print "Switch to safe mode"
	# elif pil==3:
	# 	kendali(getdata)
	# 	#nmb = int(input("-->: "))
	# 	# writeNumber(nmb)
	# 	time.sleep(0.5)
