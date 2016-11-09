#!/usr/bin/env python

from fuzzy import fuzzy

# membership function variabel cahaya
cahayarendah = [0,10,30] # trapezoid
cahayasedang = [20,40,60] # segitiga
cahayatinggi = [50,70] # trapezoid

# membership function variabel baterai
bateraisedikit = [0,1,3]
bateraisedang = [2,4,6]
bateraibanyak = [5,7]

valLDR = float(input("Input LDR: "))
valBat = float(input("Input Baterai: "))

initFuzzy = fuzzy(valLDR,valBat,1)
initFuzzy.membershipCahaya(cahayarendah,cahayasedang,cahayatinggi)
initFuzzy.membershipBaterai(bateraisedikit,bateraisedang,bateraibanyak)

getFuzCah = initFuzzy.fuzzifikasiCahaya()
getFuzBat = initFuzzy.fuzzifikasiBaterai()
getMin = initFuzzy.getMinimal()

print getFuzCah
print getFuzBat
print getMin