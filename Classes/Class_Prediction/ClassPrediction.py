#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures

class Prediction:
	def polynomialRegression(self, dataset, numCol, show=False):

		self.__dados = dataset
		self.__numCol = numCol

		self.__x = np.array(np.arange(0,len(self.__dados['DATA HORA']))).reshape(-1,1)
		self.__y = np.array(self.__dados.iloc[:,self.__numCol]).reshape(-1,1)
		
		self.__polyFeat = PolynomialFeatures(degree=10)
		self.__x01 = self.__polyFeat.fit_transform(self.__x)
		
		"TRAINING DATA"
		self.__model = linear_model.LinearRegression()
		self.__model.fit(self.__x01 ,self.__y)

		accuracy = self.__model.score(self.__x01 ,self.__y)
		
		y0 = self.__model.predict(self.__x01)
		
		if show:
			"MAKE PLOT"
			
			fig, ax = plt.subplots(figsize=(10,7))
			plt.plot(self.__dados['DATA HORA'], self.__dados.iloc[:,self.__numCol], '-m', label= self.__dados.iloc[:,self.__numCol].name)
			ax.set(xlim=(0, len(self.__dados['DATA HORA'])) , xticks=np.arange(0,len(self.__dados['DATA HORA']),8))
			
			plt.plot(y0, '--b', label=f'Prediction accuracy: {round(accuracy*100,3)}, %')
			plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
			ax.set_xlabel('DATAS', fontsize=12)
			ax.set_ylabel(self.__dados.iloc[:,numCol].name, fontsize=12)
			
			plt.xticks(rotation=45)
			plt.savefig("C:\\Users\\talis\\Desktop\\Projeto POO\\versao05\\POO\\img\\predicaoImg.png", dpi=200)

	def prediction(self, numUp):
		predict = 0

		numUp = (numUp * 4)
		for _ in range(0,numUp):
			predict += round(int(self.__model.predict(self.__polyFeat.fit_transform([[len(self.__x)+1]]))))
		
		#print("Somatorio ultimos 4 mês -> ",self.__dados.iloc[:,self.__numCol].iloc[-4:].sum())
		#print("Predição -> ",predict) 
		
		if self.__dados.iloc[:,self.__numCol].iloc[-4:].sum() > predict:
			return "BAIXA"
		else:
			return "AUMENTO"