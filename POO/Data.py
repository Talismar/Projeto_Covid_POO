#!/usr/bin/env python3
import pandas as pd
import abc

class Data(abc.ABC):
	def __init__(self, dataset):
		self.__dataset = dataset
		
		if len(self.__dataset) > 0:
			self.__data = self.__dataset['DATA HORA'][::-1]
			self.__suspeitos = self.__dataset['SUSPEITOS'][::-1]
			self.__confirmados = self.__dataset['CONFIRMADOS'][::-1]
			self.__descartados = self.__dataset['DESCARTADOS'][::-1]
			self.__obitos = self.__dataset['ÓBITOS'][::-1]
			self.__internados = self.__dataset['INTERNADOS'][::-1]
			self.__curados = self.__dataset['CURADOS'][::-1]
			self.__notificados = self.__dataset['NOTIFICADOS'][::-1]
			self.__isolamento = self.__dataset['ISOLAMENTO'][::-1]
		else:
			"Tratar os dados aqui"

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
	
	@abc.abstractmethod
	def fatalityRate(self,i,j):
		return str(round((i / j) * 100,2)) + " %"