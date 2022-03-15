#!/usr/bin/env python3
import matplotlib.pyplot as plt

class DataVisualization:
	def __init__(self, dataset):
		self.dataset = dataset

	def singlePlot(self, mes=None, ano=None, colunas=None):		
		"Listas de Cores"
		color_list=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']		
		bars = []

		plt.figure(figsize=(8, 6))
		for i in range(0,len(colunas)):
			plt.bar_label(plt.bar(colunas[i], self.dataset[self.dataset["DATA HORA"].str.contains(f'{mes}/{ano}')][colunas[i]], linewidth=2.0, color=color_list[i], label=colunas[i]))

		plt.xticks(rotation=20)
		
		plt.savefig("C:\\Users\\talis\\Desktop\\Projeto POO\\versao05\\POO\\img\\Plot_Busca_Month.png", dpi=200)

	def multiPlot(self, colunas=None):	
		"Listas de Cores"
		color_list=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']		
		
		plt.figure(figsize=(8, 6))
		for i in range(0,len(colunas)):
			plt.plot(self.dataset['DATA HORA'], self.dataset[colunas[i]], linewidth=2.0, color=color_list[i], label=colunas[i])
			
		plt.xticks(rotation=45)
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
		plt.savefig("C:\\Users\\talis\\Desktop\\Projeto POO\\versao05\\POO\\img\\Plot_Busca_Ano.png", dpi=200)

	def vizual(self):
		color_list=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']		
		
		plt.figure(figsize=(8, 6))		
		for i,j in enumerate(['SUSPEITOS', 'CONFIRMADOS', 'DESCARTADOS', 'ÓBITOS']):
			plt.plot(self.dataset['DATA HORA'], self.dataset[j], linewidth=2.0, color=color_list[i], label=j)
			
		plt.xticks(rotation=45)
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
		plt.savefig("C:\\Users\\talis\\Desktop\\Projeto POO\\versao05\\POO\\img\\plotGeral.png", dpi=200)
		