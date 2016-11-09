"""
FUZZY
Rulenya:
1. Jika penggunaan daya kecil DAN sisa daya pada baterai banyak maka switch ke panel surya
2. Jika penggunaan daya kecil DAN sisa daya pada baterai sedikit maka 
3.
4.
5.
6. 
"""

import numpy as np
from cahaya import cahaya
from baterai import baterai

class fuzzy(object):
	def __init__(self, valLDR, valBaterai, valPemakaianDaya):
		self.ldr = valLDR
		self.baterai = valBaterai
		self.daya = valPemakaianDaya

	def membershipCahaya(self,rendah,sedang,tinggi):
		self.cahayarendah = rendah
		self.cahayasedang = sedang
		self.cahayatinggi = tinggi

	def membershipBaterai(self,sedikit,sedang,banyak):
		self.bateraisedikit = sedikit
		self.bateraisedang = sedang
		self.bateraibanyak = banyak

	def membershipDaya(self,sedikit,sedang,banyak):
		self.dayasedikit = sedikit
		self.dayasedang = sedang
		self.dayabanyak = banyak

	def fuzzifikasiCahaya(self):
		paramCahaya = cahaya(self.cahayarendah,self.cahayasedang,self.cahayatinggi)
		degreeCahaya = []
		degreeCahaya.append(paramCahaya.fuzzifikasi_sedikit(self.ldr))
		degreeCahaya.append(paramCahaya.fuzzifikasi_sedang(self.ldr))
		degreeCahaya.append(paramCahaya.fuzzifikasi_tinggi(self.ldr))
		self.degreeCahaya = degreeCahaya
		return degreeCahaya

	def fuzzifikasiBaterai(self):
		paramBaterai = baterai(self.bateraisedikit,self.bateraisedang,self.bateraibanyak)
		degreeBaterai = []
		degreeBaterai.append(paramBaterai.fuzzifikasi_sedikit(self.baterai))
		degreeBaterai.append(paramBaterai.fuzzifikasi_sedang(self.baterai))
		degreeBaterai.append(paramBaterai.fuzzifikasi_banyak(self.baterai))
		self.degreeBaterai = degreeBaterai
		return degreeBaterai

	def getMinimal(self):
		minimal = []
		for i in range(3):
			for j in range(3):
				minimal.append(min(self.degreeCahaya[i],self.degreeBaterai[j]))
		return minimal
