#!/usr/bin/env python3
from tkinter import Button, Radiobutton, Entry, Label, PhotoImage, Tk, StringVar,Frame, font, messagebox
from Classes.Processing.Data_Analysis import DateAnalysis
from Classes.Visualization.Data_Visualization import DataVisualization
from Classes.Processing.ClassPrediction import Prediction
from Classes.Visualization.Settings import Settings
from os import path
from PIL import Image

"""
	Graphical interface based on the Tkinter package that implements Tk widgets as Python classes. 
	Receives all data and methods created previously and uses the friendly graphical interface for the 
	user to better understand the data. 
"""

class App(Settings):
	"Class that will create the graphical interface receiving the functions and displaying the results"
	
	def __init__(self, dataset, path_file):
		"Constructor method that receives a dataset and the path where the data"

		self.__path_file = path_file
		self.__dataset = dataset
		self.__anoInc = 2020
		self.__anoFin = 2022
		self.update_data()
		
		"Starting application"
		self.__app = Tk()
		self.configure(self.__app, self.__path_file)
		self.font_color_configuration()
		self.frames()
		self.searchMonthYear()
		self.frame_infos()
		self.painel()
		
		"Closing the application"
		self.__app.protocol("WM_DELETE_WINDOW", lambda : exit())
		self.__app.mainloop()
		
	def update_data(self, dadosGeral=False):
		"Method to update the data. If general data of true shows total data"

		self.__dataAnalysis = DateAnalysis(self.__dataset)
		"If the user does not pass any filtered data by year, it shows the complete dataset (2020 - 2022)"
		if dadosGeral:
			self.__filtredData = self.__dataAnalysis.searchYear(2020, 2022)  
		else:
			self.__filtredData = self.__dataAnalysis.searchYear(self.__anoInc, self.__anoFin)  
			
		"Use the prediction function"
		self.__pred = Prediction()

	def frames(self):        
		"General method for configuring frames"

		"Frame Options"
		self.__fr_quadro1 = Frame(self.__app, borderwidth=1, relief="sunken")
		self.__fr_quadro1.place(x=440, y=20, width=400, height=120)
		
		"Frame Information"
		self.__fr_quadro2 = Frame(self.__app, background="white", borderwidth=1, relief="sunken")
		self.__fr_quadro2.place(x=930, y=370, width=330, height=400)
		
		"Graph frame"
		self.__fr_graficos = Frame(self.__app, borderwidth=1, relief="sunken")
		self.__fr_graficos.place(x=20, y=280, width=890, height=500)
		
		"Frame Data"
		self.__fr_data = Frame(self.__app, background="white", relief="sunken")
		self.__fr_data.place(x=950,y=320, width=290, height=50)
		
		"Frame input Year - Month"
		self.__fr_Year_Month = Frame(self.__app, background="white", relief="sunken")
		self.__fr_Year_Month.place(x=10,y=145, width=550, height=95)
		
		"Frame Prediction"
		self.__fr_predicao = Frame(self.__app, background="white", relief="sunken")
		self.__fr_predicao.place(x=950,y=180, width=290, height=150)
	
	def font_color_configuration(self):
		"Method for formatting fonts and colors"
		
		"Fonts"
		self.__fonte_Bold_25 = font.Font(family="Bahnschrift SemiBold", size=25, weight="bold")
		self.__fonte_Bold_18 = font.Font(family="Bahnschrift SemiBold", size=18, weight="bold")
		
		"Colors"
		self.__letter_color = "black"
		self.__letter_background = "white"
	
	def searchMonthYear(self):
		"Method that uses Search by month and year"

		# Search by month
		Label(self.__fr_quadro1,text="Pesquisar por mês", font=self.__fonte_Bold_25).place(x=0,y=0,width=400,height=50)
		self.__searchMonth = Radiobutton(self.__fr_quadro1, text='  ', variable=StringVar(), value="Month", height=1, width=1, background="red", indicatoron=0, command=self.filtrePorMes)
		self.__searchMonth.place(x=20,y=18)          
		
		# Search by year
		Label(self.__fr_quadro1, text="Pesquisar por ano", font=self.__fonte_Bold_25).place(x=0,y=60,width=400,height=50)
		self.__search_Year = Radiobutton(self.__fr_quadro1, text='  ', variable=StringVar(), value="Year", height=1, width=1, background="red", indicatoron=0,command=self.Filter_Year)
		self.__search_Year.place(x=20,y=70)          
	
	def Filter_Year(self):
		"Method that uses Search by month and year"

		self.__search_Year.deselect()
		# Screen label
		Label(self.__fr_Year_Month, text="Informe o ano inicial:", font=self.__fonte_Bold_18).place(x=20,y=10, width=225, height=30)
		Label(self.__fr_Year_Month, text="Informe o ano final:  ", font=self.__fonte_Bold_18).place(x=20,y=50, width=225, height=30)

		# Manage the value of a widget start year and end year that the user entered
		self.YearInc = StringVar()
		self.YearFin = StringVar()

		# Position font setting within frame from start year
		self.Entry_Year_I = Entry(self.__fr_Year_Month, font=self.__fonte_Bold_18, textvariable=self.YearInc)
		self.Entry_Year_I.place(x=250,y=10, width=150, height=30)

		# Position font setting within frame from end year
		self.Entry_Year_F = Entry(self.__fr_Year_Month,font=self.__fonte_Bold_18, textvariable=self.YearFin)
		self.Entry_Year_F.place(x=250,y=50, width=150, height=30)

		# Setting Button
		Button(self.__fr_Year_Month, text='Busca por ano', command=self.checks_Erros_Year).place(x=420,y=30, width=100)
	
	def checks_Erros_Year(self):
		"Method to check user errors in application execution"

		# If user enters only the last two numbers of the starting year add 20 at the beginning
		if len(self.YearInc.get()) == 2:
			self.YearInc.set(f"20{self.YearInc.get()}")

		# If user enters only the last two numbers of the end year add 20 at the beginning
		if len(self.YearFin.get()) == 2:
			self.YearFin.set(f"20{self.YearFin.get()}")

		# If the user mistypes only 3 digits for the year or more than 4 digits, it returns an error message
		if len(self.YearInc.get()) == 3 or  len(self.YearInc.get()) > 4 or len(self.YearFin.get()) == 3 or len(self.YearFin.get()) > 4:
			messagebox.showinfo(title="Erro Preenchimento", message="ANO INVÁLIDO")
			self.Entry_Year_F.delete(0, 'end')
			self.Entry_Year_I.delete(0, 'end')
			self.Filter_Year()
			return

		# If the entered year is not within the years of the dataset, return an error message
		if int(self.YearInc.get()) < int(self.__dataset["DATA HORA"].iloc[0][6:]) or int(self.YearFin.get()) > int(self.__dataset["DATA HORA"].iloc[-1][6:]):
			messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações nessa data")
			self.Entry_Year_F.delete(0, 'end')
			self.Entry_Year_I.delete(0, 'end')    
			self.Filter_Year()
			return

		# If there is no input error, call the function search by year
		self.searcAno()
	
	def searcAno(self):
		"Search method by year, get start year and end year and return filtered dataset"

		# Clearing frame data
		self.clean_frame(self.__fr_data)
		
		# Update start and end year
		self.__anoInc = int(self.YearInc.get())
		self.__anoFin = int(self.YearFin.get())
		self.update_data()
		
		# Screen label
		Label(self.__fr_data, background=self.__letter_background, fg=self.__letter_color, text="ESCOLHA AS COLUNAS", font=self.__fonte_Bold_18).place(x=0,y=0)

		# Make a line plot
		self.col_list(multPl=True, show_button=True)
	
	def searchMonth(self):
		"Search method by month, get month and year and return a row filtered"

		# Clearing frame data
		self.clean_frame(self.__fr_data)

		# Screen label
		Label(self.__fr_data, background=self.__letter_background, fg=self.__letter_color, text="ESCOLHA AS COLUNAS", font=self.__fonte_Bold_18).place(x=0,y=0)

		# Make a bar plot
		self.col_list(simPlot=True, show_button=True)
	
	def filtrePorMes(self):
		"Label configuration in interface"
		
		# Deselect 
		self.__searchMonth.deselect()

		# Screen label
		Label(self.__fr_Year_Month, text="Informe o mês:", font=self.__fonte_Bold_18).place(x=20,y=10, width=225, height=30)
		Label(self.__fr_Year_Month, text="Informe o ano:", font=self.__fonte_Bold_18).place(x=20,y=50, width=225, height=30)

		# Manage the value of a widget start year and end year that the user entered
		self.MonthSearch = StringVar()
		self.YearSearch = StringVar()

		# Position font setting within frame from month
		Entry(self.__fr_Year_Month, font=self.__fonte_Bold_18, textvariable=self.MonthSearch).place(x=250,y=10, width=150, height=30)
		Entry(self.__fr_Year_Month,font=self.__fonte_Bold_18, textvariable=self.YearSearch).place(x=250,y=50, width=150, height=30)

		# Button YearMonth
		Button(self.__fr_Year_Month, text='Busca por mês', command=self.checks_Erros_Month).place(x=420,y=30, width=100)
	
	def checks_Erros_Month(self):
		"Method to check user errors in application execution"

		# If the month entered is between 1 and 9, add a zero in front of the entered number
		if len(self.MonthSearch.get()) == 1 and int(self.MonthSearch.get()) < 9:
			self.MonthSearch.set(f"0{self.MonthSearch.get()}")

		# If user enters only the last two numbers of the starting year add 20 at the beginning	
		if len(self.YearSearch.get()) == 2:
			self.YearSearch.set(f"20{self.YearSearch.get()}")

		# If the user mistypes only 3 digits for the year or more than 4 digits, it returns an error message	
		if len(self.YearSearch.get()) == 3 or  len(self.YearSearch.get()) > 4:
			messagebox.showinfo(title="Erro Preenchimento", message="ANO INVÁLIDO")
			self.Entry_Year_F.delete(0, 'end')
			self.Entry_Year_I.delete(0, 'end')
			self.Filter_Year()
			return

		# If the month is less than the first month in the list and the year is less than or equal to the smallest year in the list, return error
		if int(self.MonthSearch.get()) < int(self.__dataset["DATA HORA"].iloc[0][3:5]) and int(self.YearSearch.get()) <= int(self.__dataset["DATA HORA"].iloc[0][6:]):
			messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações")
			self.filtrePorMes()
			return

		# If the informed month is greater than the first month and the informed year is less than the first year in the dataset, it returns an error
		if int(self.MonthSearch.get()) > int(self.__dataset["DATA HORA"].iloc[0][3:5]) and int(self.YearSearch.get()) < int(self.__dataset["DATA HORA"].iloc[0][6:]):
			messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações")
			self.filtrePorMes()
			return

		# If the informed month is greater than the last month in the dataset and the year is greater than or equal to the last year in the dataset or the year is less than the first registered year, returns an error
		if int(self.MonthSearch.get()) > int(self.__dataset["DATA HORA"].iloc[-1][3:5]) and (int(self.YearSearch.get()) >= int(self.__dataset["DATA HORA"].iloc[-1][6:]) or int(self.YearSearch.get()) < int(self.__dataset["DATA HORA"].iloc[0][6:])):
			messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações")
			self.filtrePorMes()
			return

		# If there is no error, call the search by month method
		self.searchMonth()
	
	def multiPlot(self):
		"Function that generates a line graph based on the number of columns selected by the user"

		# Get the columns informed by the user
		listaColu = []
		for i in range(0,len(self.__Var_Cols)):
			if self.__Var_Cols[i].get() != "":
				listaColu.append(self.__Var_Cols[i].get())
				self.__Var_Selects[i].deselect()

		# Use the DataVisualization class to generate the data		
		self.__Class_plot = DataVisualization(self.__filtredData)
		
		# Make a line plot with filtered data
		self.__Class_plot.multiPlot(colunas=listaColu)
		self.GraficoMenuPrincipal(Graf_Year=True)
		
		# Clear frame2
		self.clean_frame(self.__fr_quadro2)    
		
		# Clear frame YearMonth
		self.clean_frame(self.__fr_Year_Month)
		# Returns frame information
		self.frame_infos()
	
	def simPlot(self):
		"Function that make a bar plot given a specific month and year"

		# Get the all columns given a specific month and year
		listaColu = []
		for i in range(0,len(self.__Var_Cols)):
			if self.__Var_Cols[i].get() != "":
				listaColu.append(self.__Var_Cols[i].get())
				self.__Var_Selects[i].deselect()

		# Update the data with what was entered by the user		
		self.update_data(dadosGeral=True)

		# Use the DataVisualization class to generate the data
		self.__Class_plot = DataVisualization(self.__filtredData)
		
		# Make a bar plot with filtered data
		self.__Class_plot.singlePlot(mes=self.MonthSearch.get(), ano=self.YearSearch.get(), colunas=listaColu)
		self.GraficoMenuPrincipal(Graf_Month=True)
		
		# Clear frame2
		self.clean_frame(self.__fr_quadro2)
		
		# Clear frame Month
		self.clean_frame(self.__fr_Year_Month)

		# Returns frame information
		self.frame_infos()
	
	def col_list(self, multPl=False, simPlot=False, show_button=False):
		"Method to select which plot will be used"

		# Clear frame2
		self.clean_frame(self.__fr_quadro2)
		
		# Manage the value of a widget start year and end year that the user entered
		self.__Var_Cols = []
		for i in range(0,8):
			var = StringVar()
			self.__Var_Cols.append(var)

		# Add selected values to Var_Selects list
		self.__Var_Selects = []
		for i in self.__dataset.columns:
			if i != "DATA HORA":
				self.__Var_Selects.append(i)

		# Number of positions on the Y-axis		
		numPosi_y = 5
		for i,j in enumerate(self.__dataset.columns):
			if j != "DATA HORA":
				# Label
				Label(self.__fr_quadro2, text=j, background=self.__letter_background, fg=self.__letter_color, font=self.__fonte_Bold_18).place(x=30,y=numPosi_y)

				# Buttons for columns choice
				if show_button:
					self.__Var_Selects[i-1] = Radiobutton(self.__fr_quadro2, text='  ', variable=self.__Var_Cols[i-1], value=j, height=1, width=1, background="red", indicatoron=0)
					self.__Var_Selects[i-1].place(x=5, y=7+numPosi_y)

				# Number settings for forecasting	
				else:
					self.__Var_Selects[i-1] = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color, text=f"{i}", font=self.__fonte_Bold_18)
					self.__Var_Selects[i-1].place(x=5, y=numPosi_y)
				numPosi_y += 40

		# Button MultPlot if it is true		
		if multPl:
			Button(self.__fr_quadro2, text="ENVIAR", command=self.multiPlot).place(x=10, y=350)

		# Button simPlot if it is true
		if simPlot:
			Button(self.__fr_quadro2, text="ENVIAR", command=self.simPlot).place(x=10, y=350)
	
	def frame_infos(self):
		"Configuration of the frames used in the interface"

		# Frame prediction_Information
		self.__pred.polynomialRegression(self.__dataset,4)
		
		Label(self.__fr_data, background=self.__letter_background, fg=self.__letter_color, text=f'DATA - {self.__dataAnalysis.get_data().iloc[-1]}', font=self.__fonte_Bold_25).place(x=0,y=0)
		self.__infoSuspeitos = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color, text=f"- SUSPEITOS: {self.__dataAnalysis.get_suspeitos().iloc[-1]}",font=self.__fonte_Bold_18)          
		self.__infoSuspeitos.place(x=0,y=0)
		self.__infoConfirmados = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- CONFIRMADOS: {self.__dataAnalysis.get_confirmados().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoConfirmados.place(x=0,y=40)
		self.__infoDescartados = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- DESCARTADOS: {self.__dataAnalysis.get_descartados().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoDescartados.place(x=0,y=80)
		self.__infoObitos = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- ÓBITOS: {self.__dataAnalysis.get_obitos().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoObitos.place(x=0,y=120)
		self.__infoInternados = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- INTERNADOS: {self.__dataAnalysis.get_internados().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoInternados.place(x=0,y=160)
		self.__infoCurados = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- CURADOS: {self.__dataAnalysis.get_curados().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoCurados.place(x=0,y=200)
		self.__infoNotificados = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- NOTIFICADOS: {self.__dataAnalysis.get_notificados().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoNotificados.place(x=0,y=240)
		self.__infoIsolamento = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- ISOLAMENTO: {self.__dataAnalysis.get_isolamento().iloc[-1]}",font=self.__fonte_Bold_18)
		self.__infoIsolamento.place(x=0,y=280)
		
		# fatality rate
		self.__infoFatalidade = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- TAXA FATALIDADE: {self.__dataAnalysis.fatalityRate(int(self.__dataAnalysis.get_obitos().iloc[-1]),int(self.__dataAnalysis.get_confirmados().iloc[-1]))}", font=self.__fonte_Bold_18)
		self.__infoFatalidade.place(x=0,y=320)

		# prediction trend
		self.__infoPredicao = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- TENDÊNCIA: {self.__pred.prediction(1)}",font=self.__fonte_Bold_18)
		self.__infoPredicao.place(x=0,y=360)
	
	def GraficoMenuPrincipal(self, Graf_Year=False, Graf_Month=False, Graf_Data_Total=False, Graf_Pred=False):
		"""
			Plot settings in the main menu - Returns graphics in frame_fraficos.
			If Graf_Year is true get the Plot_Busca_Ano.png image.
			If Graf_Month is true get the Plot_Busca_Month.png image.
			If Graf_Data_Total is true get the plotGeral.png image.
			If Graf_Pred is true get the predicaoImg.png image.
		"""

		# Plot by year
		if Graf_Year:
			# Clearing frame_graphics
			for i in self.__fr_graficos.winfo_children():
				i.destroy()
			# Name of saved image	
			self.__Name_Img = "Plot_Busca_Ano.png"

		# Plot by month
		if Graf_Month:
			# Clearing frame_graphics
			for i in self.__fr_graficos.winfo_children():
				i.destroy()
			# Name of saved image	
			self.__Name_Img = "Plot_Busca_Month.png"

		# Plot general data	
		if Graf_Data_Total:
			# Clearing frame_graphics
			for i in self.__fr_graficos.winfo_children():
				i.destroy()
			# Update of the data
			self.update_data(dadosGeral=True)
			# Name of saved image
			plot = DataVisualization(self.__filtredData)
			# plot general data
			plot.vizual()
			# Name of saved image
			self.__Name_Img = "plotGeral.png" 

		# Prediction plot	
		if Graf_Pred:
			# Clearing frame_graphics
			for i in self.__fr_graficos.winfo_children():
				i.destroy()
			# Name of saved image
			self.__Name_Img = "predicaoImg.png"
			
		# Reading the image to resize
		imagem = Image.open(path.join(self.__path_file + "/img/"+ self.__Name_Img))
		
		# resize
		newIm = imagem.resize(size=(950,510))
		
		# Saved the new image
		newIm.save(path.join(self.__path_file + "/img/"+ self.__Name_Img))
		
		# Display the image in the Frame
		photo = PhotoImage(file=self.__path_file + "/img/" + self.__Name_Img)
		self.__imagemGrafico = Label(self.__fr_graficos, image = photo)
		self.__imagemGrafico.image = photo
		self.__imagemGrafico.place(x=-10,y=-10,width=950,height=510)
	
	def predicao(self, coluna):
		"Prediction method, get the column you want to predict the rise or fall"

		# Clearing the elements of the prediction frame, if any previous predictions were made
		try:
			self.__fr_predicao.winfo_children()[3].destroy()
		except:
			pass

		# If there is no column selected within the dataset, return an error	
		if int(self.__Inp__Predict.get()) not in [1,2,3,4,5,6,7,8]:
			messagebox.showinfo(title="Erro Preenchimento", message="VALOR INVÁLIDO")
			self.__Inp__Predict.delete(0, 'end')
			self.predicte()
			return
		
		# Clearing frame_frame2
		self.clean_frame(self.__fr_quadro2)

		# Returns frame information
		self.frame_infos()

		# Polynomial regression method 
		self.__pred.polynomialRegression(self.__dataset,coluna, True)
		retorno = self.__pred.prediction(1)

		self.GraficoMenuPrincipal(Graf_Pred=True)
		
		# Position adjustment
		if retorno == "AUMENTO":
			x_axis = 75
		else:
			x_axis = 100

		# Label	Predict - Result of prediction
		Label(self.__fr_predicao, background=self.__letter_background, fg=self.__letter_color, text=retorno, font=self.__fonte_Bold_25).place(x=x_axis, y=100)
	
	def predicte(self):
		"Setting the prediction method"

		# Clearing the prediction and data frame
		self.clean_frame(self.__fr_predicao)
		self.clean_frame(self.__fr_data)
		
		self.col_list()
		
		# Label
		Label(self.__fr_predicao,text="Informe o nº da coluna:", background=self.__letter_background, fg=self.__letter_color, font=self.__fonte_Bold_18).place(x=0,y=5)
		self.__Inp__Predict = Entry(self.__fr_predicao, background='orange', font=self.__fonte_Bold_18)
		self.__Inp__Predict.place(x=250, y=5, height=35, width=50)
		
		# Button
		Button(self.__fr_predicao, text="Predição", font=self.__fonte_Bold_18, command=lambda : self.predicao(int(self.__Inp__Predict.get()))).place(x=90, y=50, height=40)
	
	def painel(self):
		"Main frame method (panel)"

		btn_Graf_Total = Button(self.__app, font=self.__fonte_Bold_18, text='Grafico Dos Dados', command=lambda : self.GraficoMenuPrincipal(Graf_Data_Total=True))
		btn_Graf_Total.place(x=550, y=235, height=40)
		
		btn_Graf_Pred = Button(self.__app,font=self.__fonte_Bold_18, text='Predição', command=self.predicte)
		btn_Graf_Pred.place(x=795, y=235, height=40)
