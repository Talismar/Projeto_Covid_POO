#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from DataAnalysis import dataAnalysis
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures

class Prediction:
	def polynomialRegression(self, x, y):

		self.__x = np.array(np.arange(0,len(x))).reshape(-1,1)
		self.__y = np.array(y).reshape(-1,1)
		
		plt.plot(y, '-m', label=y.name)
		
		self.__polyFeat = PolynomialFeatures(degree=10)
		self.__x01 = self.__polyFeat.fit_transform(self.__x)
		
		"TRAINING DATA"
		self.__model = linear_model.LinearRegression()
		self.__model.fit(self.__x01 ,self.__y)

		accuracy = self.__model.score(self.__x01 ,self.__y)

		y0 = self.__model.predict(self.__x01)
		
		"MAKE PLOT"
		plt.plot(y0, '--b', label=f'Prediction accuracy: {round(accuracy*100,3)}, %')
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
		plt.show()

	
	def prediction(self, teste):
		cont = 0
		print(teste)
		for i in range(0,teste):
			num=i
			
			cont += round(int(self.__model.predict(self.__polyFeat.fit_transform([[len(self.__x)+num]]))))
		print(cont)


