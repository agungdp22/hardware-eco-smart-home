import time
from time import strftime
import smbus

class i2c(object):
	def __init__(self, address):
		self.address = address
		self.bus = smbus.SMBus(1)

	def kirimData(self, value):
		self.bus.write_byte(self.address, value)
		return -1

	def bacaData(self):
		data = []
		jumlah = 0
		for i in range(0, 4):
			val = bus.read_byte(self.address)
			jumlah+=val
			data.append(val)
		data.append(jumlah)
		return jumlah