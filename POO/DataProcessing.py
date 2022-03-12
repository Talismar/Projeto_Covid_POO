#!/usr/bin/env python3

import pandas as pd
from pandas.errors import EmptyDataError
import urllib.request
import numpy as np

class dataProcessing:
	def __init__(self,dataset=None):
		if dataset == None:
			self.__dataset = self.webScraping()
		else:
			try:
				"Abrindo o arquivo"
				self.__dataset = pd.read_csv(dataset)
				
				# Delete the last row
				if "paudosferros.rn.gov.br" in str(self.__dataset.iloc[-1][1]):
					self.__dataset.drop(self.__dataset.index[-1], axis=0, inplace=True)	
		
			except EmptyDataError:
				print("Seus Dados estão vazios")

	def dataProcessing(self):        
		#Replace NaN Values with Zeros
		self.__covid_data = self.__dataset.fillna(0) 
		
		#Changing data types
		self.__covid_data = self.__covid_data.astype({'DATA HORA': np.datetime64(), 'SUSPEITOS':'int', 'CONFIRMADOS':'int', 'DESCARTADOS':'int', 'ÓBITOS':'int', 'INTERNADOS':'int', 'CURADOS':'int', 'NOTIFICADOS':'int', 'ISOLAMENTO':'int'})
		
		return self.__covid_data[::-1].reset_index(drop=True)

	def webScraping(self):
		#WebScraping of data SESAEU/PAU_DOS_FERROS_COVID-19
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

		url = "https://paudosferros.rn.gov.br/relatorio.php?id=24&rel=#"
		headers={'User-Agent':user_agent,} 

		request=urllib.request.Request(url,None,headers) #The assembled request
		response = urllib.request.urlopen(request)
		data = response.read()
		
		self.__df_list = pd.read_html(data)
		self.__df = self.__df_list[-1]
		
		# Delete the last row
		self.__df.drop(self.__df.index[-1], axis=0, inplace=True)
		
		"Aqui é pra salvar um novo dataset"
		if input("Deseja salva o Dataset [S = Sim|N - Não] -> ").lower() == "s": 
			self.__df.to_csv('new_data.csv', index=False)
			
		return self.__df