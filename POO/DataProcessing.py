#!/usr/bin/env python3

import pandas as pd
import requests
import numpy as np

class DataProcessing:
	def __init__(self,dataset=None):
		if dataset == None:
			self.__dataset = self.webScraping()
		else:
			self.__dataset = pd.read_csv(dataset)
			
			# Delete the last row
			if "paudosferros.rn.gov.br" in self.__dataset.iloc[-1][1]:
				self.__dataset.drop(self.__dataset.index[-1], axis=0, inplace=True)

	def dataProcessing(self):        
		#Replace NaN Values with Zeros
		self.__covid_data = self.__dataset.fillna(0) 
		
		#Changing data types
		self.__covid_data = self.__covid_data.astype({'DATA HORA': np.datetime64(), 'SUSPEITOS':'int', 'CONFIRMADOS':'int', 'DESCARTADOS':'int', 'ÓBITOS':'int', 'INTERNADOS':'int', 'CURADOS':'int', 'NOTIFICADOS':'int', 'ISOLAMENTO':'int'})

		return self.__covid_data

	def webScraping(self):
		#WebScraping of data SESAEU/PAU_DOS_FERROS_COVID-19
		self.__url = 'https://paudosferros.rn.gov.br/relatorio.php?id=24&rel=#'
		self.__html = requests.get(self.__url).content
		self.__df_list = pd.read_html(self.__html)
		self.__df = self.__df_list[-1]

		# Delete the last row
		self.__df.drop(self.__df.index[-1], axis=0, inplace=True)
		
		"Aqui é pra salvar um novo dataset"
		if input("Deseja salva o Dataset [S = Sim|N - Não] -> ").lower() == "s": 
			self.__df.to_csv('new_data.csv', index=False)
			
		return self.__df

if __name__ == "__main__":
	#data = DataProcessing("C:\\Users\\talis\\Desktop\\Projeto POO\\Projeto_Covid_POO\\data.csv")
	data = DataProcessing()