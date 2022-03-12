from tkinter import Button, Checkbutton, Entry, Label, PhotoImage, Tk, Canvas, IntVar,Frame, font
from DataProcessing import dataProcessing
from DataAnalysis import DateAnalysis
from dataVisualization import *
from Prediction import *
from os import path
from PIL import Image

class App():
    def __init__(self, dataset, caminho):
        self.caminho = caminho
        self.dataset = dataset
        self.__app = Tk()
        self.configure()
        
        self.searchMonthYear()
        self.teste()
        self.painel()
        self.__app.mainloop()

    def configure(self):
        self.__app.configure(background="white")
        self.__app.overrideredirect(False)
        self.__app.geometry("{0}x{1}+0+0".format(self.__app.winfo_screenwidth(), self.__app.winfo_screenheight()))
        self.__app.title('Info COVID-19')

        "Logo Projeto"
        self.__img = PhotoImage(file="C:\\Users\\talis\\Desktop\\Projeto POO\\Projetov3\\version04\\Projeto_Covid_POO\\POO\\Logo1.png")
        self.__logo = Label(self.__app, image=self.__img)
        self.__logo.place(x=1000,y=0,width=520,height=180)

        "LogoIFRN Projeto"
        self.__imgIFRN = PhotoImage(file="C:\\Users\\talis\\Desktop\\Projeto POO\\Projetov3\\version04\\Projeto_Covid_POO\\POO\\IFRN.png")
        self.__logoIFRN = Label(self.__app, image=self.__imgIFRN)
        self.__logoIFRN.place(x=0,y=0,width=520,height=180)

    def searchMonthYear(self):
        fr_quadro1 = Frame(self.__app, borderwidth=1, relief="sunken")
        fr_quadro1.place(x=507, y=150, width=500, height=120)
        
        self.__labelFont3 = font.Font(family="Bahnschrift SemiBold", size=25, weight="bold")
        self.__searchMonth = Checkbutton(fr_quadro1, text="Pesquisar por mês", font=self.__labelFont3, command=self.filtrePorMes)
        self.__searchMonth.place(x=0,y=0,width=500,height=50)
        
        self.__searchYear = Checkbutton(fr_quadro1, text="Pesquisar por ano", font=self.__labelFont3, command=self.filtrePorAno)
        self.__searchYear.place(x=0,y=60,width=500,height=50)
    
    def searcAno(self):
        dataAnal = DateAnalysis(dadosLimpo)
        filtredData = dataAnal.searchYear(int(self.YearInc.get()),int(self.YearFin.get()))
        plot = dataVisualization(filtredData)
        
        Label(self.__app, text="Escolha a quantidade de colunas -", bg='white', font=self.labelFont2).place(x=1050,y=220, width=370, height=30)
        
        self.NCols = Entry(self.__app, font=self.labelFont2)
        self.NCols.place(x=1430,y=220, width=50, height=30)

        #Label(self.__app, text="Informe o ano final:  ", font=self.labelFont2).place(x=20,y=220, width=225, height=30)


    def filtrePorAno(self):
        
        Label(self.__app, text="Informe o ano inicial:", font=self.labelFont2).place(x=20,y=180, width=225, height=30)
        Label(self.__app, text="Informe o ano final:  ", font=self.labelFont2).place(x=20,y=220, width=225, height=30)
        
        self.YearInc = Entry(self.__app, font=self.labelFont2)
        self.YearInc.place(x=270,y=180, width=150, height=30)
        self.YearFin = Entry(self.__app,font=self.labelFont2)
        self.YearFin.place(x=270,y=220, width=150, height=30)

        Button(self.__app, text='Buscar', command=self.searcAno).place(x=320,y=270)
        
    def filtrePorMes(self):
        pass

    def teste(self):
        fr_quadro1 = Frame(self.__app, borderwidth=1, relief="sunken")
        fr_quadro1.place(x=1100, y=350, width=400, height=400)
    
        dataAnal = DateAnalysis(self.dataset)

        pred = Prediction()
        pred.polynomialRegression(self.dataset,4)
        
        self.labelFont2 = font.Font(family="Bahnschrift SemiBold", size=18, weight="bold")
        Label(self.__app, bg='white', text=f'DATA - {dataAnal.get_data().iloc[-1]}', font=self.__labelFont3).place(x=1150,y=300, width=300)
        self.__infoSuspeitos = Label(fr_quadro1,text=f"- SUSPEITOS: {dataAnal.get_suspeitos().iloc[-1]}",font=self.labelFont2)
        self.__infoSuspeitos.place(x=0,y=0)
        self.__infoConfirmados = Label(fr_quadro1,text=f"- CONFIRMADOS: {dataAnal.get_confirmados().iloc[-1]}",font=self.labelFont2)
        self.__infoConfirmados.place(x=0,y=40)
        self.__infoDescartados = Label(fr_quadro1,text=f"- DESCARTADOS: {dataAnal.get_descartados().iloc[-1]}",font=self.labelFont2)
        self.__infoDescartados.place(x=0,y=80)
        self.__infoObitos = Label(fr_quadro1,text=f"- ÓBITOS: {dataAnal.get_obitos().iloc[-1]}",font=self.labelFont2)
        self.__infoObitos.place(x=0,y=120)
        self.__infoInternados = Label(fr_quadro1,text=f"- INTERNADOS: {dataAnal.get_internados().iloc[-1]}",font=self.labelFont2)
        self.__infoInternados.place(x=0,y=160)
        self.__infoCurados = Label(fr_quadro1,text=f"- CURADOS: {dataAnal.get_curados().iloc[-1]}",font=self.labelFont2)
        self.__infoCurados.place(x=0,y=200)
        self.__infoNotificados = Label(fr_quadro1,text=f"- NOTIFICADOS: {dataAnal.get_notificados().iloc[-1]}",font=self.labelFont2)
        self.__infoNotificados.place(x=0,y=240)
        self.__infoIsolamento = Label(fr_quadro1,text=f"- ISOLAMENTO: {dataAnal.get_isolamento().iloc[-1]}",font=self.labelFont2)
        self.__infoIsolamento.place(x=0,y=280)
        
        "Taxa de fatalidade"
        self.__infoFatalidade = Label(fr_quadro1,text=f"- TAXA FATALIDADE: {dataAnal.fatalityRate(int(dataAnal.get_obitos().iloc[-1]),int(dataAnal.get_confirmados().iloc[-1]))}", font=self.labelFont2)
        self.__infoFatalidade.place(x=0,y=320)
        self.__infoIsolamento = Label(fr_quadro1,text=f"- TENDÊNCIA: {pred.prediction(1)}",font=self.labelFont2)
        self.__infoIsolamento.place(x=0,y=360)
    
    def GraficoM(self,fr_graficos):
        
        dataAnal = DateAnalysis(dadosLimpo)
        filtredData = dataAnal.searchYear(2021, 2022)
        plot = dataVisualization(filtredData)
        "Gera a imagem"
        plot.vizual()

        imagem = Image.open(path.join(self.caminho,"plotGeral.png" ))
        
        newIm = imagem.resize(size=(950,460))
        newIm.save(path.join(self.caminho,"plotGeral.png" ))
        photo = PhotoImage(file=caminho + "\\plotGeral.png")
        self.__imagemGrafico = Label(fr_graficos, image = photo)
        self.__imagemGrafico.image = photo
        self.__imagemGrafico.place(x=-10,y=-20,width=950,height=460)

    def predicao(self, coluna,fr_graficos):
        pred = Prediction()
        pred.polynomialRegression(self.dataset,coluna, True)
        pred.prediction(int(coluna))

        imagem = Image.open(path.join(self.caminho,"predicaoImg.png" ))
        
        newIm = imagem.resize(size=(950,460))
        newIm.save(path.join(self.caminho,"predicaoImg.png" ))
        photo = PhotoImage(file=caminho + "\\predicaoImg.png")
        self.__imagemGrafico = Label(fr_graficos, image = photo)
        self.__imagemGrafico.image = photo
        self.__imagemGrafico.place(x=-10,y=-20,width=950,height=460)

    def painel(self):
        fr_graficos = Frame(self.__app, borderwidth=1, relief="sunken")
        fr_graficos.place(x=100, y=350, width=900, height=550)
        
        buttonGraficoMain = Button(self.__app, text='Imagem Principal', command=lambda : self.GraficoM(fr_graficos))
        buttonGraficoMain.place(x=500, y=300)
        
        buttonGraficoMain = Button(self.__app, text='Predição', command=lambda : self.predicao(2,fr_graficos))
        buttonGraficoMain.place(x=400, y=300)

"Opcional passar arquivo ou não - senão passar o algoritmo baixa"
#
dataProc = dataProcessing("C:\\Users\\talis\\Desktop\\Projeto POO\\Projetov3\\version04\\Projeto_Covid_POO\\data.csv")
caminho =path.dirname(__file__)

"Dados limpo e na ordem correta aqui"
dadosLimpo = dataProc.dataProcessing()


App(dadosLimpo, caminho)