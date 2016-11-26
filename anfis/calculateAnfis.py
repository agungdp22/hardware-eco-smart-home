from trainingData import trainingData as tryAnfis
import numpy as np
import anfis
import time

anf = tryAnfis(epochs=10)
anf.training()
print "Training Selesai"
x = 100
y = 1
while True:
	# x=int(input())
	# y=int(input())
	prediksi = anf.keputusan(x,y)
	x=x-1
	y=y+1
	print x,y
	if x<5:
		x=100
	if y==20:
		y=1
	time.sleep(1)
	# print prediksi[0][0]