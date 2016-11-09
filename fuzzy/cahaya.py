from __future__ import division
from __future__ import absolute_import

class cahaya(object):
	def __init__(self,cahayarendah,cahayasedang,cahayatinggi):
		self.daerahsedikit = cahayarendah
		self.daerahsedang = cahayasedang
		self.daerahtinggi = cahayatinggi

	def fuzzifikasi_sedikit(self,val):
		if(val<=self.daerahsedikit[1]):
			cahaya_sedikit = 1.0
		elif(val>self.daerahsedikit[1] and val<self.daerahsedikit[2]):
			cahaya_sedikit = float((self.daerahsedikit[2]-val)/(self.daerahsedikit[2]-self.daerahsedikit[1]))
		else:
			cahaya_sedikit = 0.0
		return cahaya_sedikit

	def fuzzifikasi_sedang(self,val):
		if(val==self.daerahsedang[1]):
			cahaya_sedang = 1.0
		elif(val<self.daerahsedang[1] and val>self.daerahsedang[0]):
			cahaya_sedang = float((val-self.daerahsedang[0])/(self.daerahsedang[1]-self.daerahsedang[0]))
			tes = 1
		elif(val>self.daerahsedang[1] and val<self.daerahsedang[2]):
			cahaya_sedang = (self.daerahsedang[2]-val)/(self.daerahsedang[2]-self.daerahsedang[1])
		else:
			cahaya_sedang = 0.0
		return cahaya_sedang

	def fuzzifikasi_tinggi(self,val):
		if(val>=self.daerahtinggi[1]):
			cahaya_tinggi = 1.0
		elif(val<self.daerahtinggi[1] and val>self.daerahtinggi[0]):
			cahaya_tinggi = float((val-self.daerahtinggi[0])/(self.daerahtinggi[1]-self.daerahtinggi[0]))
		else:
			cahaya_tinggi = 0.0
		return cahaya_tinggi
		