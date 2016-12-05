#!/usr/bin/env python
import time
import numpy as np
from I2C_Arduino.i2c import i2c
from API.getAPI import getAPI
from API.postAPI import postAPI
from anfis.trainingData import trainingData as tryAnfis
from konekSocket import listeningServer
from random import randint


def safemode(persentase, jumlahdaya):
	predik = anf.keputusan(persentase,jumlahdaya)
	return predik

# Training data dulu
# anf = tryAnfis(epochs=10)
# anf.training()
print "Training Data Selesai...."

# alamat i2c, disamain dgn yg di arduino->0x68
address = 0x68
headerAPI = {'Authorization': 'coegsekali ', "Content-Type": "application/json"}

postdata = postAPI(headerAPI)
getdata = getAPI(headerAPI)
konekArduino = i2c(address)
print "Device ready..."

while True:
	# x=int(input("Persentase: "))
	# y=int(input("Daya: "))
	# postdata.postBaterai(x)
	# isSafe = safemode(x,y)
	# if isSafe:
	# 	postdata.safeMode()
	# 	print "Switch to safe mode"
	# send = getdata.cekBuff()
	# print send
	# if send!="berubah":
	# 	konekArduino.kendaliPerangkat(send)
	# time.sleep(5)
	listeningServer()
	daya = randint(1,20)
	print daya
	postdata.postDaya(daya)

