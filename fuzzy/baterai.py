from __future__ import division
from __future__ import absolute_import

class baterai(object):
	def __init__(self,baterairendah,bateraisedang,bateraitinggi):
		self.daerahsedikit = baterairendah
		self.daerahsedang = bateraisedang
		self.daerahtinggi = bateraitinggi

	def fuzzifikasi_sedikit(self,val):
		if(val<=self.daerahsedikit[1]):
			baterai_sedikit = 1.0
		elif(val>self.daerahsedikit[1] and val<self.daerahsedikit[2]):
			baterai_sedikit = float((self.daerahsedikit[2]-val)/(self.daerahsedikit[2]-self.daerahsedikit[1]))
		else:
			baterai_sedikit = 0.0
		return baterai_sedikit

	def fuzzifikasi_sedang(self,val):
		if(val==self.daerahsedang[1]):
			baterai_sedang = 1.0
		elif(val<self.daerahsedang[1] and val>self.daerahsedang[0]):
			baterai_sedang = float((val-self.daerahsedang[0])/(self.daerahsedang[1]-self.daerahsedang[0]))
			tes = 1
		elif(val>self.daerahsedang[1] and val<self.daerahsedang[2]):
			baterai_sedang = (self.daerahsedang[2]-val)/(self.daerahsedang[2]-self.daerahsedang[1])
		else:
			baterai_sedang = 0.0
		return baterai_sedang

	def fuzzifikasi_banyak(self,val):
		if(val>=self.daerahtinggi[1]):
			baterai_tinggi = 1.0
		elif(val<self.daerahtinggi[1] and val>self.daerahtinggi[0]):
			baterai_tinggi = float((val-self.daerahtinggi[0])/(self.daerahtinggi[1]-self.daerahtinggi[0]))
		else:
			baterai_tinggi = 0.0
		return baterai_tinggi
		