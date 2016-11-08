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

valSensLDR = 25		#  2  3  4  5  6  7  8
parameter1 = cahaya(0,10,30,20,40,60,50,70)
cahaya_rendah = parameter1.fuzzifikasi_sedikit(valSensLDR)
cahaya_sedang = parameter1.fuzzifikasi_sedang(valSensLDR)
cahaya_tinggi = parameter1.fuzzifikasi_tinggi(valSensLDR)

valSensBaterai = 3.5
parameter2 = baterai(0,1,3,2,4,6,5,7)
baterai_rendah = parameter2.fuzzifikasi_sedikit(valSensBaterai)
baterai_sedang = parameter2.fuzzifikasi_sedang(valSensBaterai)
baterai_tinggi = parameter2.fuzzifikasi_tinggi(valSensBaterai)

print cahaya_rendah
print cahaya_sedang
print cahaya_tinggi

print baterai_rendah
print baterai_sedang
print baterai_tinggi
