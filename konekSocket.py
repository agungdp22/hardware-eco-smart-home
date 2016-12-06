#!/usr/bin/env python
from socketIO_client import SocketIO, LoggingNamespace
from I2C_Arduino.i2c import i2c
import time

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
	socketIO.wait(seconds=20)

