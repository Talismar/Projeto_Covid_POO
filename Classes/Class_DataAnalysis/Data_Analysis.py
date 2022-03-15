#!/usr/bin/env python3
import pandas as pd
from Classes.Class_Data import ClassData
from numpy import arange

class DateAnalysis(ClassData.Data):
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
				if i[3:] not in DateAnalysis.myListDate:
					DateAnalysis.myListDate.append(i[3:])
					DateAnalysis.myList.append(self.searchMonth(i[3:5],i[6:]))
			
			new_dataset = pd.DataFrame({"DATA HORA":DateAnalysis.myListDate})
			
			for i in pd.DataFrame(DateAnalysis.myList).columns:
				new_dataset[i] = pd.DataFrame(DateAnalysis.myList)[i]

			DateAnalysis.myListDate.clear()
			DateAnalysis.myList.clear()
			"Retorna a soma de meses"
			return new_dataset

		else:
			listaDatas = []
			for i in super().get_data():
				if i[3:] not in listaDatas and i[6:] == str(anoFinal):
					listaDatas.append(i[3:])
					DateAnalysis.myList.append(self.searchMonth(i[3:5],i[6:]))

			new_dataset = pd.DataFrame({"DATA HORA":listaDatas})
			
			for i in pd.DataFrame(DateAnalysis.myList).columns:
				new_dataset[i] = pd.DataFrame(DateAnalysis.myList)[i]
			
			DateAnalysis.myListDate.clear()
			DateAnalysis.myList.clear()
			"Retorna a soma de meses"
			return new_dataset
		
	def searchMonth(self, month, year, numMonth=False):
		if '0' not in month and len(month) == 1:
			month = str(0) + month

		"Indentifica quantidade de ocorrencias em um dado mês"
		search = super().get_dataset()[super().get_dataset()["DATA HORA"].str.contains(f'/{month}/{year}')]

		if numMonth:
			return len(search)
		else:
			return search.iloc[:,arange(1,9,1)].sum()
	
	def fatalityRate(self, totalObitos=None, totalConfirmados=None, totalRate=False):
		"Polimorfismo"
		if totalRate:
			return super().fatalityRate()
		else:
			return str(round((totalObitos / totalConfirmados) * 100,2)) + " %"

	def __del__(self):
		"Destrutor"
		#print("Objeto destruido")