from __future__ import division
class baterai(object):
	def __init__(self, titik1, titik2, titik3, titik4, titik5, titik6, titik7, titik8):
		self.titik1 = titik1	# 0
		self.titik2 = titik2	# 10
		self.titik3 = titik3 	# 20
		self.titik4 = titik4 	# 30
		self.titik5 = titik5 	# 40
		self.titik6 = titik6 	# 50
		self.titik7 = titik7 	# 60
		self.titik8 = titik8 	# 70

	def fuzzifikasi_sedikit(self,val):
		if(val<=self.titik2):
			baterai_sedikit = 1.0
		elif(val>self.titik2 and val<self.titik3):
			baterai_sedikit = float((self.titik3-val)/(self.titik3-self.titik2))
		else:
			baterai_sedikit = 0.0
		return baterai_sedikit

	def fuzzifikasi_sedang(self,val):
		if(val==self.titik5):
			baterai_sedang = 1.0
		elif(val<self.titik5 and val>self.titik4):
			baterai_sedang = float((val-self.titik4)/(self.titik5-self.titik4))
			tes = 1
		elif(val>self.titik5 and val<self.titik6):
			baterai_sedang = (self.titik6-val)/(self.titik6-self.titik5)
		else:
			baterai_sedang = 0.0
		return baterai_sedang

	def fuzzifikasi_tinggi(self,val):
		if(val>=self.titik8):
			baterai_tinggi = 1.0
		elif(val<self.titik8 and val>self.titik7):
			baterai_tinggi = float((val-self.titik7)/(self.titik8-self.titik7))
		else:
			baterai_tinggi = 0.0
		return baterai_tinggi
		