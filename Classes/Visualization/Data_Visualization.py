#!/usr/bin/env python3
import matplotlib.pyplot as plt

class DataVisualization:
	"""
		Receives the data (which can be the dataset, filtered dataset or simply a dataset row) 
		processed and analyzed and returns a plot that can be simple bar (singlePlot) or with various 
		comparative information (multiPlot and vizual)
	"""

	def __init__(self, dataset):
		"Receives the dataset"
		self.dataset = dataset
	
	def singlePlot(self, mes=None, ano=None, colunas=None):		
		"Takes a month and a year to return a plot with that user-specified period."

		# Variable that stores a list of colors to generate different colors for each column
		color_list=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']	
		
		plt.figure(figsize=(8, 6))
		# For each column generates a bar inside the chart with the specific value
		for i in range(0,len(colunas)):
			plt.bar_label(plt.bar(colunas[i], self.dataset[self.dataset["DATA HORA"].str.contains(f'{mes}/{ano}')][colunas[i]], linewidth=2.0, color=color_list[i], label=colunas[i]))
		# Rotation of the label on the X axis
		plt.xticks(rotation=20)
		# Save the plot in a directory called img
		plt.savefig("/home/talismar/Desktop/Covid/Projeto_Covid_POO/img/Plot_Busca_Month.png", dpi=200)
	
	def multiPlot(self, colunas=None):	
		"Receives one or more columns for the Y axis, the X axis being the DATA column"

		# Variable that stores a list of colors to generate different colors for each column
		color_list=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']		
		
		plt.figure(figsize=(8, 6))
		# For each column chosen by the user, it generates a line with the respective value in the plot
		for i in range(0,len(colunas)):
			plt.plot(self.dataset['DATA HORA'], self.dataset[colunas[i]], linewidth=2.0, color=color_list[i], label=colunas[i])
		# Rotation of the label on the X axis	
		plt.xticks(rotation=45)
		# Legend location at the top center of the plot
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
		# Save the plot in a directory called img
		plt.savefig("/home/talismar/Desktop/Covid/Projeto_Covid_POO/img/Plot_Busca_Ano.png", dpi=200)
	
	def vizual(self):
		"Method to generate a line chart with the general information from the 4 main columns"

		# Variable that stores a list of colors to generate different colors for each column
		color_list=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']		
		
		plt.figure(figsize=(8, 6))
		# For each column chosen, it generates a line with the respective value in the plot
		for i,j in enumerate(['SUSPEITOS', 'CONFIRMADOS', 'DESCARTADOS', 'ÓBITOS']):
			plt.plot(self.dataset['DATA HORA'], self.dataset[j], linewidth=2.0, color=color_list[i], label=j)
		# Rotation of the label on the X axis	
		plt.xticks(rotation=45)
		# Legend location at the top center of the plot
		plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=8)
		# Save the plot in a directory called img
		plt.savefig("/home/talismar/Desktop/Covid/Projeto_Covid_POO/img/plotGeral.png", dpi=200)
		