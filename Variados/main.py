#!/usr/bin/env python3

from DataProcessing import DataProcessing
from Data import Data
from dataAnalysis import dataAnalysis
from dataVisualization import *
from Prediction import *

if __name__=='__main__':
	"Aqui voce mudar o path pra o data surjo kkkkk"
	lim = DataProcessing('data.csv')
	dadosLimpo = lim.dataProcessing()
	
		
	busca = dataAnalysis(dadosLimpo)
	filtredData = busca.buscaAno(2019, 2021)
	#filtredData.drop(['index'], axis=1, inplace=True)
	#print(filtredData.dtypes)
	filtredData = filtredData.astype({'DATA HORA': 'string'})
	x = []
	for i in filtredData['DATA HORA']:
		x.append(i)
	print(x)
	plot = dataVisualization()
	plot.singlePlot(filtredData['DATA HORA'][::-1], filtredData['ÓBITOS'][::-1])
	
	

	
	