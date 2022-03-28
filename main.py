#!/usr/bin/env python3
from Classes.Processing.Data_Processing import DataProcessing
from Classes.Visualization.App import App
from os import path

path_file = path.dirname(__file__)

# Optional pass file or not - otherwise the algorithm downloads the dataset on the site (webScraping)
dataProc = DataProcessing(path_file + "/data.csv")

# If the inserted dataset is empty, return an error
if dataProc.retorno == "Seus Dados estão vazios":
	print(dataProc.retorno)

# If not, open the interface
else:
	dadosLimpo = dataProc.dataProcessing()
	
	# If you need to see documentation for any method use name.__doc__
	# For example
	# print(App.__doc__)
	
	App(dadosLimpo, path_file)