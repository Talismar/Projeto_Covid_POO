#!/usr/bin/env python3
import pandas as pd
from pandas.errors import EmptyDataError
import urllib.request
import numpy as np


class DataProcessing:
	'''
	Make the following checks:
	1- If it doesn't receive a dataset, it uses the webScraping method to download it directly from the site;
	2- If the informed dataset is empty, it returns the message: Your data is empty.
	If none of the cases occurs, proceed to process the data and save in a csv file.
	'''
	
	# Variable that will return a message if there is an error in the dataset.
	retorno=""
	
	def __init__(self,dataset=None):
		"Constructor that can receive a dataset or not."	
		# If it doesn't receive a dataset it uses the webScraping method to download it directly from the website.
		if dataset == None:
			self.__dataset = self.webScraping()
		
		# If it receives the dataset, it tries to open this dataset and puts it in the variable self.__dataset.
		else:
			try:
				"Abrindo o arquivo"
				self.__dataset = pd.read_csv(dataset)
				
				# Delete the last line if it contains paudosferros.rn.gov.br
				if "paudosferros.rn.gov.br" in str(self.__dataset.iloc[-1][1]):
					self.__dataset.drop(self.__dataset.index[-1], axis=0, inplace=True)	
			# If the informed dataset is empty, it returns the error message
			except EmptyDataError:
				DataProcessing.retorno= "Seus Dados estão vazios"

	def dataProcessing(self):     
		"Data processing and cleaning > return clean data"   

		# Replace NaN Values with Zeros
		self.__covid_data = self.__dataset.fillna(0) 
		
		# Changing data types
		self.__covid_data = self.__covid_data.astype({'DATA HORA': 'object', 'SUSPEITOS':'int', 'CONFIRMADOS':'int', 'DESCARTADOS':'int', 'ÓBITOS':'int', 'INTERNADOS':'int', 'CURADOS':'int', 'NOTIFICADOS':'int', 'ISOLAMENTO':'int'})
		print(self.__covid_data)
		return self.__covid_data[::-1].reset_index(drop=True)

	def webScraping(self):
		"WebScraping of data SESAEU/PAU_DOS_FERROS_COVID-19 > return data"

		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		url = "https://paudosferros.rn.gov.br/relatorio.php?id=24&rel=#"
		headers={'User-Agent':user_agent,} 
		
		# The assembled request.
		request=urllib.request.Request(url,None,headers)
		response = urllib.request.urlopen(request)
		data = response.read()
		
		# turn data variable into an html table
		self.__df_list = pd.read_html(data)
		self.__df = self.__df_list[-1]
		
		# Delete the last row
		self.__df.drop(self.__df.index[-1], axis=0, inplace=True)
		
		# Save the table in a csv file
		if input("Deseja salva o Dataset [S = Sim|N - Não] -> ").lower() == "s": 
			self.__df.to_csv('new_data.csv', index=False)
			
		return self.__df
