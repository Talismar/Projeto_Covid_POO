#!/usr/bin/env python3
import pandas as pd
from DataProcessing import dataProcessing
from DataAnalysis import DateAnalysis
from dataVisualization import *
from Prediction import *

if __name__=='__main__':
	"Opcional passar arquivo ou não - senão passar o algoritmo baixa"
	
	dataProc = dataProcessing("C:\\Users\\talis\\Desktop\\Projeto POO\\Projetov3\\version04\\Projeto_Covid_POO\\data.csv")
	
	"Dados limpo e na ordem correta aqui"
	dadosLimpo = dataProc.dataProcessing()
	
	#print(dadosLimpo)
	
	dataAnal = DateAnalysis(dadosLimpo)
	"Sum Month"
	#print(dataAnal.searchMonth("8",'2020'))

	"Sum Year"
	filtredData = dataAnal.searchYear(2021, 2022)
	#print(filtredData)

	"Taxa de fatalidade de todo o dataset"
	#print(dataAnal.fatalityRate(totalRate=True))
	"Taxa de fatalidade especifica"
	#print(dataAnal.fatalityRate(filtredData['ÓBITOS'][1],filtredData['CONFIRMADOS'][1]))

	plot = dataVisualization(filtredData)
	#plot.singlePlot(filtredData['DATA HORA'], filtredData['CONFIRMADOS'])
	plot.multiPlot(8)
	#plot.vizual()

	""" pred = Prediction()
	pred.polynomialRegression(dadosLimpo,4, True)
	pred.prediction(1) """