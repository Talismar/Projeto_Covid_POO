from tkinter import Button, Radiobutton, Entry, Label, PhotoImage, Tk, StringVar,Frame, font, messagebox
from Classes.Class_DataProcessing.Data_Processing import DataProcessing
from Classes.Class_DataAnalysis.Data_Analysis import DateAnalysis
from Classes.Class_DataVisualization.Data_Visualization import DataVisualization
from Classes.Class_Prediction.ClassPrediction import Prediction
from os import path
from PIL import Image

class Settings():
    def configure(self, app, path_file):
        "Configuração da tela"
        app.configure(background="white")
        app.geometry("1280x800")    
        app.title("INFO COVID-19")
        #app.resizable(True,True)
        app.maxsize(width=1280, height=800)
        app.minsize(width=1280, height=800)

        "Logo Projeto"
        self.__img = PhotoImage(file= path_file + "\\img\\" + "Logo1.png")
        self.__logo = Label(app, image=self.__img)
        self.__logo.place(x=870,y=0,width=400,height=120)

        "LogoIFRN Projeto"
        self.__imgIFRN = PhotoImage(file= path_file + "\\img\\"  + "IFRN.png")
        self.__logoIFRN = Label(app, image=self.__imgIFRN)
        self.__logoIFRN.place(x=0,y=0,width=400,height=120)        

    def clean_frame(self, frame):
        for i in frame.winfo_children():
            i.destroy()

class App(Settings):
    def __init__(self, dataset, path_file):
        self.__path_file = path_file
        self.__dataset = dataset
        self.__anoInc = 2020
        self.__anoFin = 2022
        self.update_data()

        "Iniciando aplicativo"
        self.__app = Tk()
        self.configure(self.__app, self.__path_file)
        self.font_color_configuration()
        self.frames()
        self.searchMonthYear()
        self.frame_infos()
        self.painel()

        "Fechando o aplicativo"
        self.__app.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.__app.mainloop()

    def update_data(self, dadosGeral=False):
        self.__dataAnalysis = DateAnalysis(self.__dataset)
        
        if dadosGeral:
            self.__filtredData = self.__dataAnalysis.searchYear(2020, 2022)  
        else:
            self.__filtredData = self.__dataAnalysis.searchYear(self.__anoInc, self.__anoFin)  
        
        "Classe prediction"
        self.__pred = Prediction()

    def frames(self):        
        "Opções"
        self.__fr_quadro1 = Frame(self.__app, borderwidth=1, relief="sunken")
        self.__fr_quadro1.place(x=440, y=20, width=400, height=120)
        
        "Informações"
        self.__fr_quadro2 = Frame(self.__app, background="white", borderwidth=1, relief="sunken")
        self.__fr_quadro2.place(x=930, y=370, width=330, height=400)

        "Frame do grafico"
        self.__fr_graficos = Frame(self.__app, borderwidth=1, relief="sunken")
        self.__fr_graficos.place(x=20, y=280, width=890, height=500)

        "Frame Data"
        self.__fr_data = Frame(self.__app, background="white", relief="sunken")
        self.__fr_data.place(x=950,y=320, width=290, height=50)

        "Frame Imputs Ano - Mês"
        self.__fr_Year_Month = Frame(self.__app, background="white", relief="sunken")
        self.__fr_Year_Month.place(x=10,y=145, width=550, height=95)

        "Frame Predições"
        self.__fr_predicao = Frame(self.__app, background="white", relief="sunken")
        self.__fr_predicao.place(x=950,y=180, width=290, height=150)

    def font_color_configuration(self):
        "Formatos de fontes"
        self.__fonte_Bold_25 = font.Font(family="Bahnschrift SemiBold", size=25, weight="bold")
        self.__fonte_Bold_18 = font.Font(family="Bahnschrift SemiBold", size=18, weight="bold")

        "Colors"
        self.__letter_color = "black"
        self.__letter_background = "white"

    def searchMonthYear(self):
        "Pesquisar Month"
        Label(self.__fr_quadro1,text="Pesquisar por mês", font=self.__fonte_Bold_25).place(x=0,y=0,width=400,height=50)
        self.__searchMonth = Radiobutton(self.__fr_quadro1, text='  ', variable=StringVar(), value="Month", height=1, width=1, background="red", indicatoron=0, command=self.filtrePorMes)
        self.__searchMonth.place(x=20,y=18)           
        
        "Pesquisar Year"
        Label(self.__fr_quadro1, text="Pesquisar por ano", font=self.__fonte_Bold_25).place(x=0,y=60,width=400,height=50)
        self.__search_Year = Radiobutton(self.__fr_quadro1, text='  ', variable=StringVar(), value="Year", height=1, width=1, background="red", indicatoron=0,command=self.Filter_Year)
        self.__search_Year.place(x=20,y=70)           
    
    def Filter_Year(self):
        self.__search_Year.deselect()
        Label(self.__fr_Year_Month, text="Informe o ano inicial:", font=self.__fonte_Bold_18).place(x=20,y=10, width=225, height=30)
        Label(self.__fr_Year_Month, text="Informe o ano final:  ", font=self.__fonte_Bold_18).place(x=20,y=50, width=225, height=30)
        
        self.YearInc = StringVar()
        self.YearFin = StringVar()

        self.Entry_Year_I = Entry(self.__fr_Year_Month, font=self.__fonte_Bold_18, textvariable=self.YearInc)
        self.Entry_Year_I.place(x=250,y=10, width=150, height=30)
        
        self.Entry_Year_F = Entry(self.__fr_Year_Month,font=self.__fonte_Bold_18, textvariable=self.YearFin)
        self.Entry_Year_F.place(x=250,y=50, width=150, height=30)

        Button(self.__fr_Year_Month, text='Busca por ano', command=self.checks_Erros_Year).place(x=420,y=30, width=100)

    def checks_Erros_Year(self):
        if len(self.YearInc.get()) == 2:
            self.YearInc.set(f"20{self.YearInc.get()}")

        if len(self.YearFin.get()) == 2:
            self.YearFin.set(f"20{self.YearFin.get()}")

        if len(self.YearInc.get()) == 3 or  len(self.YearInc.get()) > 4 or len(self.YearFin.get()) == 3 or len(self.YearFin.get()) > 4:
            messagebox.showinfo(title="Erro Preenchimento", message="ANO INVÁLIDO")
            self.Entry_Year_F.delete(0, 'end')
            self.Entry_Year_I.delete(0, 'end')
            self.Filter_Year()
            return

        if int(self.YearInc.get()) < int(self.__dataset["DATA HORA"].iloc[0][6:]) or int(self.YearFin.get()) > int(self.__dataset["DATA HORA"].iloc[-1][6:]):
            messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações nessa data")
            self.Entry_Year_F.delete(0, 'end')
            self.Entry_Year_I.delete(0, 'end')    
            self.Filter_Year()
            return
        
        self.searcAno()

    def searcAno(self):
        "Limpando frame data"
        self.clean_frame(self.__fr_data)

        "Atualizar o ano inicial e final"
        self.__anoInc = int(self.YearInc.get())
        self.__anoFin = int(self.YearFin.get())
        self.update_data()

        
        Label(self.__fr_data, background=self.__letter_background, fg=self.__letter_color, text="ESCOLHA AS COLUNAS", font=self.__fonte_Bold_18).place(x=0,y=0)
        self.col_list(multPl=True, show_button=True)

    def searchMonth(self):
        "Limpando frame data"
        self.clean_frame(self.__fr_data)

        Label(self.__fr_data, background=self.__letter_background, fg=self.__letter_color, text="ESCOLHA AS COLUNAS", font=self.__fonte_Bold_18).place(x=0,y=0)
        self.col_list(simPlot=True, show_button=True)

    def filtrePorMes(self):
        self.__searchMonth.deselect()
        Label(self.__fr_Year_Month, text="Informe o mês:", font=self.__fonte_Bold_18).place(x=20,y=10, width=225, height=30)
        Label(self.__fr_Year_Month, text="Informe o ano:", font=self.__fonte_Bold_18).place(x=20,y=50, width=225, height=30)
        
        self.MonthSearch = StringVar()
        self.YearSearch = StringVar()

        Entry(self.__fr_Year_Month, font=self.__fonte_Bold_18, textvariable=self.MonthSearch).place(x=250,y=10, width=150, height=30)
        Entry(self.__fr_Year_Month,font=self.__fonte_Bold_18, textvariable=self.YearSearch).place(x=250,y=50, width=150, height=30)
        
        Button(self.__fr_Year_Month, text='Busca por mês', command=self.checks_Erros_Month).place(x=420,y=30, width=100)

    def checks_Erros_Month(self):
        if len(self.MonthSearch.get()) == 1 and int(self.MonthSearch.get()) < 9:
            self.MonthSearch.set(f"0{self.MonthSearch.get()}")

        if len(self.YearSearch.get()) == 2:
            self.YearSearch.set(f"20{self.YearSearch.get()}")
        
        if len(self.YearSearch.get()) == 3 or  len(self.YearSearch.get()) > 4:
            messagebox.showinfo(title="Erro Preenchimento", message="ANO INVÁLIDO")
            self.Entry_Year_F.delete(0, 'end')
            self.Entry_Year_I.delete(0, 'end')
            self.Filter_Year()
            return

        if int(self.MonthSearch.get()) < int(self.__dataset["DATA HORA"].iloc[0][3:5]) and int(self.YearSearch.get()) <= int(self.__dataset["DATA HORA"].iloc[0][6:]):
            messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações")
            self.filtrePorMes()
            return 

        if int(self.MonthSearch.get()) > int(self.__dataset["DATA HORA"].iloc[0][3:5]) and int(self.YearSearch.get()) < int(self.__dataset["DATA HORA"].iloc[0][6:]):
            messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações")
            self.filtrePorMes()
            return 

        if int(self.MonthSearch.get()) > int(self.__dataset["DATA HORA"].iloc[-1][3:5]) and (int(self.YearSearch.get()) >= int(self.__dataset["DATA HORA"].iloc[-1][6:]) or int(self.YearSearch.get()) < int(self.__dataset["DATA HORA"].iloc[0][6:])):
            messagebox.showinfo(title="Erro Preenchimento", message="Você não possui informações")
            self.filtrePorMes()
            return 

        self.searchMonth()

    def multiPlot(self):
        listaColu = []
        for i in range(0,len(self.__Var_Cols)):
            if self.__Var_Cols[i].get() != "":
                listaColu.append(self.__Var_Cols[i].get())
                self.__Var_Selects[i].deselect()

        self.__Class_plot = DataVisualization(self.__filtredData)
        
        "Gerei a imagem aqui"
        self.__Class_plot.multiPlot(colunas=listaColu)
        
        self.GraficoMenuPrincipal(Graf_Year=True)

        "Limpando o frame2"
        self.clean_frame(self.__fr_quadro2)    

        "Limpando o frame"
        self.clean_frame(self.__fr_Year_Month)

        self.frame_infos()

    def simPlot(self):
        listaColu = []
        for i in range(0,len(self.__Var_Cols)):
            if self.__Var_Cols[i].get() != "":
                listaColu.append(self.__Var_Cols[i].get())
                self.__Var_Selects[i].deselect()
        
        self.update_data(dadosGeral=True)
        self.__Class_plot = DataVisualization(self.__filtredData)
        
        "Gerei a imagem aqui"
        self.__Class_plot.singlePlot(mes=self.MonthSearch.get(), ano=self.YearSearch.get(), colunas=listaColu)
        self.GraficoMenuPrincipal(Graf_Month=True)
       
        "Limpando o frame2"
        self.clean_frame(self.__fr_quadro2)
        
        "Limpando o frame do Month"
        self.clean_frame(self.__fr_Year_Month)
            
        self.frame_infos()

    def col_list(self, multPl=False, simPlot=False, show_button=False):
        "Limpando o frame2"
        self.clean_frame(self.__fr_quadro2)

        self.__Var_Cols = []
        for i in range(0,8):
            var = StringVar()
            self.__Var_Cols.append(var)
        
        self.__Var_Selects = []
        for i in self.__dataset.columns:
            if i != "DATA HORA":
                self.__Var_Selects.append(i)
        
        numPosi_y = 5
        for i,j in enumerate(self.__dataset.columns):
            if j != "DATA HORA":
                Label(self.__fr_quadro2, text=j, background=self.__letter_background, fg=self.__letter_color, font=self.__fonte_Bold_18).place(x=30,y=numPosi_y)

                if show_button:
                    self.__Var_Selects[i-1] = Radiobutton(self.__fr_quadro2, text='  ', variable=self.__Var_Cols[i-1], value=j, height=1, width=1, background="red", indicatoron=0)
                    self.__Var_Selects[i-1].place(x=5, y=7+numPosi_y)

                else:
                    self.__Var_Selects[i-1] = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color, text=f"{i}", font=self.__fonte_Bold_18)
                    self.__Var_Selects[i-1].place(x=5, y=numPosi_y)
                numPosi_y += 40

        if multPl:
            Button(self.__fr_quadro2, text="ENVIAR", command=self.multiPlot).place(x=10, y=350)

        if simPlot:
            Button(self.__fr_quadro2, text="ENVIAR", command=self.simPlot).place(x=10, y=350)
            
    def frame_infos(self):
        "Predição do frame_Informações"
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
        
        "Taxa de fatalidade"
        self.__infoFatalidade = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- TAXA FATALIDADE: {self.__dataAnalysis.fatalityRate(int(self.__dataAnalysis.get_obitos().iloc[-1]),int(self.__dataAnalysis.get_confirmados().iloc[-1]))}", font=self.__fonte_Bold_18)
        self.__infoFatalidade.place(x=0,y=320)
        self.__infoIsolamento = Label(self.__fr_quadro2, background=self.__letter_background, fg=self.__letter_color,text=f"- TENDÊNCIA: {self.__pred.prediction(1)}",font=self.__fonte_Bold_18)
        self.__infoIsolamento.place(x=0,y=360)
    
    def GraficoMenuPrincipal(self, Graf_Year=False, Graf_Month=False, Graf_Data_Total=False, Graf_Pred=False):
        
        if Graf_Year:
            "Limpando o frame_graficos"
            self.clean_frame(self.__fr_graficos)
            
            self.__Name_Img = "Plot_Busca_Ano.png"

        if Graf_Month:
            "Limpando o frame_graficos"
            self.clean_frame(self.__fr_graficos)
            
            self.__Name_Img = "Plot_Busca_Month.png"

        if Graf_Data_Total:
            "Limpando o frame_graficos"
            self.clean_frame(self.__fr_graficos)

            self.update_data(dadosGeral=True)
            "Gera a imagem - Precisamos fazer uma logica pra pegar o ano atual"
            plot = DataVisualization(self.__filtredData)
            
            plot.vizual()
            self.__Name_Img = "plotGeral.png" 
            
        if Graf_Pred:
            "Limpando o frame_graficos"
            self.clean_frame(self.__fr_graficos)

            self.__Name_Img = "predicaoImg.png"

        "Lendo a imagem pra redimenciona-lo"
        imagem = Image.open(path.join(self.__path_file + "\\img\\", self.__Name_Img))
        
        "Redimencionando"
        newIm = imagem.resize(size=(950,510))
        
        "Salvando a imagem com o novo tamanho"
        newIm.save(path.join(self.__path_file + "\\img\\", self.__Name_Img))

        "Apresenta a imagem no Frame"
        photo = PhotoImage(file=self.__path_file + "\\img\\" + self.__Name_Img)
        self.__imagemGrafico = Label(self.__fr_graficos, image = photo)
        self.__imagemGrafico.image = photo
        self.__imagemGrafico.place(x=-10,y=-10,width=950,height=510)

    def predicao(self, coluna):
        if int(self.__Inp__Predict.get()) not in [1,2,3,4,5,6,7,8]:
            messagebox.showinfo(title="Erro Preenchimento", message="VALOR INVÁLIDO")
            self.__Inp__Predict.delete(0, 'end')
            self.predicte()
            return

        "Limpando o frame_quadro2"
        self.clean_frame(self.__fr_quadro2)
        
        self.frame_infos()

        self.__pred.polynomialRegression(self.__dataset,coluna, True)
        retorno = self.__pred.prediction(1)
        self.GraficoMenuPrincipal(Graf_Pred=True)

        if retorno == "AUMENTO":
            aux = 75
        else:
            aux = 100
        
        Label(self.__fr_predicao, background=self.__letter_background, fg=self.__letter_color, text=retorno, font=self.__fonte_Bold_25).place(x=aux, y=100)
    
    def predicte(self):
        "Limpando o frame predicao e data"
        self.clean_frame(self.__fr_predicao)
        self.clean_frame(self.__fr_data)

        self.col_list()

        Label(self.__fr_predicao,text="Informe o nº da coluna:", background=self.__letter_background, fg=self.__letter_color, font=self.__fonte_Bold_18).place(x=0,y=5)
        self.__Inp__Predict = Entry(self.__fr_predicao, background='orange', font=self.__fonte_Bold_18)
        self.__Inp__Predict.place(x=250, y=5, height=35, width=50)
        
        Button(self.__fr_predicao, text="Predicao", font=self.__fonte_Bold_18, command=lambda : self.predicao(int(self.__Inp__Predict.get()))).place(x=90, y=50, height=40)
        
    def painel(self):
        btn_Graf_Total = Button(self.__app, font=self.__fonte_Bold_18, text='Grafico Dos Dados', command=lambda : self.GraficoMenuPrincipal(Graf_Data_Total=True))
        btn_Graf_Total.place(x=550, y=235, height=40)
        
        btn_Graf_Pred = Button(self.__app,font=self.__fonte_Bold_18, text='Predição', command=self.predicte)
        btn_Graf_Pred.place(x=795, y=235, height=40)

"Opcional passar arquivo ou não - senão passar o algoritmo baixa"
path_file = path.dirname(__file__)

dataProc = DataProcessing(path_file + "\\data.csv")

if dataProc.retorno == "Seus Dados estão vazios":
    print(dataProc.retorno)
else:
    "Dados limpo e na ordem correta aqui"
    dadosLimpo = dataProc.dataProcessing()
    App(dadosLimpo, path_file)