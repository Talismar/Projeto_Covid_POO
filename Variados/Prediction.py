#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures


class Predict:
	def __init__(self, y, x=None) -> None:
		self.__y = y
		self.__x = x
		
		if self.__x == None:
			self.__x = np.arange(0,len(self.__y))
			
	def vizualicao(self):
		#print(self.__y)
		print(len(self.__x),len(self.__y))
		plt.plot(self.__y, '-m')
		plt.show()
		
	def fit(self, degree):
		self.__x = np.array(self.__x).reshape(-1,1)
		self.__y = np.array(self.__y).reshape(-1,1)
		self.__polyFeat = PolynomialFeatures(degree=degree)
		x = self.__polyFeat.fit_transform(self.__x)
		
		"TRAINING DATA"
		self.__model = linear_model.LinearRegression()
		self.__model.fit(x,self.__y)
		accuracy = self.__model.score(x,self.__y)
		
		print('Accuracy > ', round(accuracy*100,3), "%")
		
		print(len(self.__x),len(self.__y))
		plt.plot(self.__y, '-m')
		y0 = self.__model.predict(x)
		plt.plot(y0, '--b')
		plt.show()
		
	def prediction(self, num):
		print("PREDICTION")
		up_after = 1
		
		print(f'Prediction - Cases after {up_after}: ', end='')
		print(round(int(self.__model.predict(self.__polyFeat.fit_transform([[len(self.__y)+up_after]])))))
		
		