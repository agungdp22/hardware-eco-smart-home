#!/usr/bin/env python
from socketIO_client import SocketIO, LoggingNamespace
import json
from I2C_Arduino.i2c import i2c

host = 'agungdp.agri.web.id'
port = 2016

socketIO = SocketIO(host, port, LoggingNamespace)
konekArduino = i2c(0x68)

def getRekues(*args):
	data=args[0]
	konekArduino.kendaliPerangkat(data)
	return args[0]

def listeningServer():
	print "Listening server..."
	socketIO.on('kendaliPerangkat', getRekues)
	# PIR = konekArduino.bacaData()
	# print "PIR=",PIR
	# if PIR>0:
	# 	konekArduino.kirimData(PIR)
	# 	socketIO.emit('kendaliPerangkat',{'pesan':'bos ada maling bos'})
	# else:
	# 	socketIO.emit('kendaliPerangkat',{'pesan':'bos aman bos'})
	socketIO.wait(seconds=300)

