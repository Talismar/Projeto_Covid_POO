#!/usr/bin/env python3
import abc

'''
Abstract class that receives information from the already processed dataset and stores it in their respective variables
'''
class Data(abc.ABC):
	def __init__(self, dataset):
		# Receive the dataset and store it in encapsulated (private) variables
		self.__dataset = dataset
		self.__data = self.__dataset['DATA HORA']
		self.__suspeitos = self.__dataset['SUSPEITOS']
		self.__confirmados = self.__dataset['CONFIRMADOS']
		self.__descartados = self.__dataset['DESCARTADOS']
		self.__obitos = self.__dataset['ÓBITOS']
		self.__internados = self.__dataset['INTERNADOS']
		self.__curados = self.__dataset['CURADOS']
		self.__notificados = self.__dataset['NOTIFICADOS']
		self.__isolamento = self.__dataset['ISOLAMENTO']
	
	# Getters and setters used to protect and manipulate data.
	def get_dataset(self):
		return self.__dataset
	def get_data(self):
		return self.__data
	def get_suspeitos(self):
		return self.__suspeitos
	def get_confirmados(self):
		return self.__confirmados
	def get_descartados(self):
		return self.__descartados
	def get_obitos(self):
		return self.__obitos
	def get_internados(self):
		return self.__internados
	def get_curados(self):
		return self.__curados
	def get_notificados(self):
		return self.__notificados
	def get_isolamento(self):
		return self.__isolamento
	
	def set_dataset(self, dataset):
		self.__dataset = dataset
	def set_data(self, data):
		self.__data = data
	def set_suspeitos(self, suspeitos):
		self.__suspeitos = suspeitos
	def set_confirmados(self, confirmados):
		self.__confirmados = confirmados
	def set_descartados(self, descartados):
		self.__descartados = descartados
	def set_obitos(self, obitos):
		self.__obitos = obitos
	def set_internados(self, internados):
		self.__internados = internados
	def set_curados(self, curados):
		self.__curados = curados
	def set_notificados(self, notificados):
		self.__notificados = notificados
	def set_isolamento(self, isolamento):
		self.__isolamento = isolamento
	
	# Abstract method that returns the fatality rate
	@abc.abstractmethod
	def fatalityRate(self):
		"Retorna a taxa de fatalidade de todo o dataset"
		return str(round((self.__obitos.sum() / self.__confirmados.sum()) * 100,2)) + " %"
	
	# Represents Data class objects as a string, returning the most recent information for each column of the dataset
	def __str__(self):
		return f'Data - {self.__data.iloc[-1]}\nSuspeitos - {self.__suspeitos.iloc[-1]}\nConfirmados - {self.__confirmados.iloc[-1]}\nDescartados - {self.__descartados.iloc[-1]}\nÓbitos - {self.__obitos.iloc[-1]}\nInternados - {self.__internados.iloc[-1]}\nCurados - {self.__curados.iloc[-1]}\nNotificados - {self.__notificados.iloc[-1]}\nIsolamento - {self.__isolamento.iloc[-1]}'