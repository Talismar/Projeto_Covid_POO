#!/usr/bin/env python3
import pandas as pd
from Classes.Processing import ClassData
from numpy import arange

class DateAnalysis(ClassData.Data):
	"Inherits the Data class to use the data in the search by month  and search by year methods"
	
	"Lists that will store the dates searched by the user"
	myListDate = []
	myList = []
	
	"Constructor method that will receive a dataset"
	def __init__(self, dataset):
		super().__init__(dataset)
	
	def searchYear(self, anoInicial, anoFinal):
		"""
			Search method by year. Gets a start year and end year to filter the information in this time range.
			Returns a specific year
		"""	

		if anoInicial != anoFinal:
			# Variable that will receive the years informed if they are different years
			myListDataFramesYear = []
			
			# Loop to receive all values from the start year to the end year.
			while anoInicial <= anoFinal:
				myListDataFramesYear.append(super().get_dataset()[super().get_dataset()["DATA HORA"].str.contains(f'/{str(anoInicial)}')])
				# Each interaction the start year increases by 1 year
				anoInicial+=1
			
			# Concat the filtered data
			self.__searc = pd.concat(myListDataFramesYear, ignore_index=True)
			
			# Adds the filtered data in the respective lists
			for i in self.__searc['DATA HORA']:
				if i[3:] not in DateAnalysis.myListDate:
					# Each element of the filtered data is added to the myListDate without the day
					DateAnalysis.myListDate.append(i[3:])
					# Each element of the filtered data is added to the myList separating month and year (with searchMonth)
					DateAnalysis.myList.append(self.searchMonth(i[3:5],i[6:]))
			
			# Create a new dataset with the filtered information
			new_dataset = pd.DataFrame({"DATA HORA":DateAnalysis.myListDate})
			
			# Create a new dataframe with just the months and years separated
			for i in pd.DataFrame(DateAnalysis.myList).columns:
				new_dataset[i] = pd.DataFrame(DateAnalysis.myList)[i]
			
			# Clean the lists so as not to accumulate the data added to each filter made by the user
			DateAnalysis.myListDate.clear()
			DateAnalysis.myList.clear()
			# Returns a dataset with all information filtered
			return new_dataset
		
		# If the start year is the same as the end year informed by the user
		else:
			# Create a list that will receive the data
			listaDatas = []
			for i in super().get_data():
				# Condition to separate by months of the same year
				if i[3:] not in listaDatas and i[6:] == str(anoFinal):
					listaDatas.append(i[3:])
					# Each element of the filtered data is added to the myList separating month and year
					DateAnalysis.myList.append(self.searchMonth(i[3:5],i[6:]))
			# Create a new dataset with the filtered information
			new_dataset = pd.DataFrame({"DATA HORA":listaDatas})
			
			# Create a new dataframe with just the months and years separated
			for i in pd.DataFrame(DateAnalysis.myList).columns:
				new_dataset[i] = pd.DataFrame(DateAnalysis.myList)[i]
			
			# Clean the lists so as not to accumulate the data added to each filter made by the user
			DateAnalysis.myListDate.clear()
			DateAnalysis.myList.clear()
			
			# Returns a dataset with all information filtered
			return new_dataset
		
	def searchMonth(self, month, year, numMonth=False):
		"""
			Search method by month in a specific year. Gets a month and the year to filter the information in this time range
			Return sum of the month
		"""

		# Adds a 0 in front if the user has only assigned one number in the month
		if '0' not in month and len(month) == 1:
			month = str(0) + month

		# Identify number of occurrences in a given month
		search = super().get_dataset()[super().get_dataset()["DATA HORA"].str.contains(f'/{month}/{year}')]
		
		# If given a single month, returns the row with the values of each column
		if numMonth:
			return len(search)
		# If not, returns the sum of the past months
		else:
			return search.iloc[:,arange(1,9,1)].sum()
	
	def fatalityRate(self, totalObitos=None, totalConfirmados=None, totalRate=False):
		"Abstract method for calculating the fatality rate."
		
		# Used for summing all the value of the general dataset 
		if totalRate:
			return super().fatalityRate()
		# Used for a specific date
		else:
			return str(round((totalObitos / totalConfirmados) * 100,2)) + " %"
	
	def __del__(self):
		"Destructor method"
		#print("Objeto destruído")