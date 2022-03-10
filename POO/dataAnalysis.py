#!/usr/bin/env python3
import pandas as pd
from Data import Data
from numpy import arange

class dataAnalysis(Data):
	myListDate = []
	myList = []

	def __init__(self, dataset):
		super().__init__(dataset)
		
	def searchYear(self, anoInicial, anoFinal):
		if anoInicial != anoFinal:
			myListDataFramesYear = []

			while anoInicial <= anoFinal:
				myListDataFramesYear.append(super().get_dataset()[super().get_dataset()["DATA HORA"].str.contains(f'/{str(anoInicial)}')])
				anoInicial+=1	

			"Concat"				
			self.__searc = pd.concat(myListDataFramesYear, ignore_index=True)
			
			for i in self.__searc['DATA HORA']:
				if i[3:] not in dataAnalysis.myListDate:
					dataAnalysis.myListDate.append(i[3:])
					dataAnalysis.myList.append(self.searchMonth(i[3:5],i[6:]))
			
			new_dataset = pd.DataFrame({"DATA HORA":dataAnalysis.myListDate})
			
			for i in pd.DataFrame(dataAnalysis.myList).columns:
				new_dataset[i] = pd.DataFrame(dataAnalysis.myList)[i]

			"Retorna a soma de meses"
			return new_dataset

		else:
			self.__searcFi = super().get_dataset()[super().get_dataset()["DATA HORA"].str.contains(f'/{str(anoFinal)}')]

			for i in self.__searcFi['DATA HORA']:
				if i[3:] not in dataAnalysis.myListDate:
					dataAnalysis.myListDate.append(i[3:])
					dataAnalysis.myList.append(self.searchMonth(i[3:5],i[6:]))
			
			"Retorna a soma de meses"
			new_dataset = pd.DataFrame({"DATA HORA":dataAnalysis.myListDate})
			
			for i in pd.DataFrame(dataAnalysis.myList).columns:
				new_dataset[i] = pd.DataFrame(dataAnalysis.myList)[i]
			
			"Retorna a soma de meses"
			return new_dataset
		
	def searchMonth(self, month, year):
		if '0' not in month and len(month) == 1:
			month = str(0) + month

		searc = super().get_dataset()[super().get_dataset()["DATA HORA"].str.contains(f'/{month}/{year}')]
		
		
		#return len(searc)
		
		return searc.iloc[:,arange(1,9,1)].sum()
	
	def fatalityRate(self,i,j):
		
		print(super().fatalityRate(i,j))

if __name__ == "__main__":
	data = dataAnalysis("C:\\Users\\talis\\Desktop\\Projeto POO\\Projetov3\\new_data.csv")
	