#!/usr/bin/env python3
import pandas as pd
from Data import Data


class dataAnalysis (Data):
	
	def __init__(self, dataset):
		super().__init__(dataset)
		

	def buscaAno(self,anoInicial, anoFinal):
		
		inicio = f'{anoInicial}-01-01'
		final = f'{anoFinal}-12-31'
		#Busca por Ano
		selecao = (super().get_dataset()['DATA HORA']  >= inicio) & (super().get_dataset()['DATA HORA']  <= final)
		
		
		df_filtrado = super().get_dataset()[selecao].reset_index()
		
		#print(df_filtrado)
		return df_filtrado
		
	def buscaMes(self):
		pass
		
		