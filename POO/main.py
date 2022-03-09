#!/usr/bin/env python3

from DataProcessing import DataProcessing
from Data import Data
from dataAnalysis import dataAnalysis
from dataVisualization import *
from Prediction import *

if __name__=='__main__':
	"Opcional passar arquivo ou não - senão passar o algoritmo baixa"
	lim = DataProcessing("C:\\Users\\talis\\Desktop\\Projeto POO\\new_data.csv")
	dadosLimpo = lim.dataProcessing()
	
	busca = dataAnalysis(dadosLimpo)
	filtredData = busca.searchYear(2021, 2021)
	#busca.searchMonth("7",'2021')
	print(filtredData)
	
	plot = dataVisualization()
	#plot.singlePlot(filtredData['DATA HORA'], filtredData['CONFIRMADOS'])
	plot.multiPlot(3,filtredData[::-1])
	