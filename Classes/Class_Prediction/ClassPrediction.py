#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures

'''
Receives a column specified by the user (from the entire dataset) and returns a prediction of the next month if there will be an increase or decrease in the face of the trained data.
'''

class Prediction:
	# Receives a dataset and the specific column number to perform the prediction
	def polynomialRegression(self, dataset, numCol, show=False):
		# Variables that will receive the dataset and column number chosen by the user
		self.__dados = dataset
		self.__numCol = numCol
		# New shape to an array without changing its data for X and Y
		self.__x = np.array(np.arange(0,len(self.__dados['DATA HORA']))).reshape(-1,1)
		self.__y = np.array(self.__dados.iloc[:,self.__numCol]).reshape(-1,1)
		# Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree.
		self.__polyFeat = PolynomialFeatures(degree=10)
		# Fit to data, then transform it.
		self.__x01 = self.__polyFeat.fit_transform(self.__x)
		
		# Training data
		self.__model = linear_model.LinearRegression()
		# Fit to data
		self.__model.fit(self.__x01 ,self.__y)
		# Calculates accuracy based on X and Y axis values
		accuracy = self.__model.score(self.__x01 ,self.__y)
		# Y-axis polynomial prediction
		y0 = self.__model.predict(self.__x01)
		
		if show:
			# Make a line plot
			fig, ax = plt.subplots(figsize=(10,7))
			# X-axis is the DATE TIME column and the Y-axis is the column selected by the user
			plt.plot(self.__dados['DATA HORA'], self.__dados.iloc[:,self.__numCol], '-m', label= self.__dados.iloc[:,self.__numCol].name)
			# Label configuration and initial and final distance
			ax.set(xlim=(0, len(self.__dados['DATA HORA'])) , xticks=np.arange(0,len(self.__dados['DATA HORA']),8))
			# Prediction plot based on trained data
			plt.plot(y0, '--b', label=f'Prediction accuracy: {round(accuracy*100,3)}, %')
			# Legend location at the top center of the plot
			plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
			# Y-axis and X-axis labels
			ax.set_xlabel('DATAS', fontsize=12)
			ax.set_ylabel(self.__dados.iloc[:,numCol].name, fontsize=12)
			# Rotation of the label on the X axis
			plt.xticks(rotation=45)
			# Save the plot in a directory called img
			plt.savefig("img/predicaoImg.png", dpi=200)
	
	# Method used for prediction based on trained data
	def prediction(self, numUp):
		predict = 0
		# Interaction based on 4 weeks equivalent to one month's data
		numUp = (numUp * 4)
		for _ in range(0,numUp):
			predict += round(int(self.__model.predict(self.__polyFeat.fit_transform([[len(self.__x)+1]]))))
		
		print("Somatorio ultimos 4 mês -> ",self.__dados.iloc[:,self.__numCol].iloc[-4:].sum())
		print("Predição -> ",predict) 
		
		# Returns a message to the user if there was an increase or decrease trend
		if self.__dados.iloc[:,self.__numCol].iloc[-4:].sum() > predict:
			return "BAIXA"
		else:
			return "AUMENTO"