#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures

class Prediction:
	def polynomialRegression(self,x,y):
		x = np.array(x).reshape(-1,1)
		y = np.array(y).reshape(-1,1)
		#print(len(x),len(y))
		plt.plot(y, '-m', label='SUSPEITOS')
		#plt.show()
		
		polyFeat = PolynomialFeatures(degree=10)
		x = polyFeat.fit_transform(x)
		
		"TRAINING DATA"
		model = linear_model.LinearRegression()
		model.fit(x,y)
		accuracy = model.score(x,y)
		print('Accuracy > ', round(accuracy*100,3), "%")
		y0 = model.predict(x)
		
		"MAKE PLOT"
		plt.plot(y0, '--b', label=f'Prediction accuracy: {round(accuracy*100,3)}, %')
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
		plt.show()
		
		
		print("PREDICTION")
		up_after = 1
	
		print(x.sum())
		print(f'Prediction - Cases after {up_after}: ', end='')
		print(round(int(model.predict(polyFeat.fit_transform([[len(x)+up_after]])))))
