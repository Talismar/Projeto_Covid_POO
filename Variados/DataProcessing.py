#!/usr/bin/env python3

import pandas as pd
import requests
import numpy as np

class DataProcessing:
	def __init__(self,dataset=None):
		if dataset == None:
			self.__dataset = self.webScraping()
			
		self.__dataset = dataset
		
	def dataProcessing(self):
		#Dataset information and check the missing values
		self.covid_data = pd.read_csv(self.__dataset)
		self.covid_data.drop(self.covid_data.index[len(self.covid_data)-1], inplace=True) # Delete the last row
		self.covid_data = self.covid_data.fillna(0) #Replace NaN Values with Zeros
		
		#Changing data types
		self.covid_data = self.covid_data.astype({'DATA HORA': 'datetime64', 'SUSPEITOS':'int', 'CONFIRMADOS':'int', 'DESCARTADOS':'int', 'ÓBITOS':'int', 'INTERNADOS':'int', 'CURADOS':'int', 'NOTIFICADOS':'int', 'ISOLAMENTO':'int'})
		
		return self.covid_data
	
	
	def webScraping(self):
		#WebScraping of data SESAEU/PAU_DOS_FERROS_COVID-19
		url = 'https://paudosferros.rn.gov.br/relatorio.php?id=24&rel=#'
		html = requests.get(url).content
		df_list = pd.read_html(html)
		self.df = df_list[-1]
		print(self.df)
		self.df.to_csv('data.csv', index=False)
		return self.df