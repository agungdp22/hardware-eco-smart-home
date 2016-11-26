# sudo python -m pip install anfis
# sudo pip install -U scikit-fuzzy

import anfis
import membership # import fungsi di folder membership
import numpy
import copy

class trainingData(object):
	def __init__(self, epochs):
		self.epochs = epochs

	def training(self):
		ts = numpy.loadtxt("anfis/traindaya.txt", usecols=[0,1,2])
		X = ts[:,0:2]
		Y = ts[:,2]

		mf = [[['gaussmf',{'mean':-11.,'sigma':5.}],['gaussmf',{'mean':-8.,'sigma':5.}],['gaussmf',{'mean':-14.,'sigma':20.}],['gaussmf',{'mean':-7.,'sigma':7.}]],
		            [['gaussmf',{'mean':-10.,'sigma':20.}],['gaussmf',{'mean':-20.,'sigma':11.}],['gaussmf',{'mean':-9.,'sigma':30.}],['gaussmf',{'mean':-10.5,'sigma':5.}]]]

		mfc = membership.membershipfunction.MemFuncs(mf)
		self.anf = anfis.ANFIS(X, Y, mfc)
		self.anf.trainHybridJangOffLine(epochs=self.epochs)
		# print round(anf.consequents[-1][0],6)
		# print round(anf.consequents[-2][0],6)
		# print round(anf.fittedValues[9][0],6)
		if round(self.anf.consequents[-1][0],6) == -5.275538 and round(self.anf.consequents[-2][0],6) == -1.990703 and round(self.anf.fittedValues[9][0],6) == 0.002249:
			print 'test is good'
		# anf.plotErrors()
		# anf.plotResults()
		# return self.anf

	def keputusan(self,dayaBaterai,pemakaianDaya):
		model = self.anf
		parameter = numpy.array([[dayaBaterai,pemakaianDaya],[1,1]])
		prediksi = anfis.predict(model,parameter)
		print prediksi[0][0]
		if prediksi[0][0]>0.5:
			print "Switch to panel surya"
			return True
		else:
			print "PLN Mode"
			return False
		# return prediksi[0][0]