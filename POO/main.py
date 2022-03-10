#!/usr/bin/env python3
import pandas as pd
from DataProcessing import DataProcessing
from Data import Data
from DataAnalysis import dataAnalysis
from dataVisualization import *
from Prediction import *

if __name__=='__main__':
	"Opcional passar arquivo ou não - senão passar o algoritmo baixa"
	lim = DataProcessing("C:\\Users\\talis\\Desktop\\Projeto POO\\new_data.csv")
	dadosLimpo = lim.dataProcessing()
	
	busca = dataAnalysis(dadosLimpo)
	filtredData = busca.searchYear(2021, 2022)

	data1 = dataAnalysis(filtredData)
	for i, j in zip(filtredData['ÓBITOS'],filtredData['CONFIRMADOS']):
			data1.fatalityRate(i,j)

	#busca.searchMonth("8",'2020')

	#busca.searchMonth("7",'2021')
	#print(filtredData)
	
	#plot = dataVisualization()
	#plot.singlePlot(filtredData['DATA HORA'], filtredData['CONFIRMADOS'])
	#plot.multiPlot(3,filtredData[::-1])
	
	

	""" pred = Prediction()
	pred.polynomialRegression(dadosLimpo['DATA HORA'][:-5], dadosLimpo['CONFIRMADOS'][:-5])
	
	if isinstance(busca,dataAnalysis):
		pred.prediction(busca.searchMonth("02", "2022")) """