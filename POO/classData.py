import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures

class Data:
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
	
    """ def __str__(self):
        return f'Data\n{self.__data}\nSuspeitos\n{self.__suspeitos}\nConfirmados\n{self.__confirmados}\nDescartados\n{self.__descartados}\nÓbitos\n{self.__obitos}\nInternados\n{self.__internados}\nCurados\n{self.__curados}\nNotificados{self.__notificados}\nIsolamento\n{self.__isolamento}' """
    
    """ def __add__(self):
        pass """

class DataProcessing:
    def __init__(self,dataset=None):
        if dataset == None:
           dataset = self.webScraping()
        
        self.__dataset = dataset

    def dataProcessing(self):
        #Dataset information and check the missing values
        self.covid_data = pd.read_csv(self.__dataset)
        self.covid_data.drop(148 , inplace=True) # Delete the row 148 from dataFrame
        self.covid_data = self.covid_data.fillna(0) #Replace NaN Values with Zeros
        
        #Changing data types
        self.covid_data = self.covid_data.astype({'DATA HORA':np.datetime64(), 'SUSPEITOS':'int', 'CONFIRMADOS':'int', 'DESCARTADOS':'int', 'ÓBITOS':'int', 'INTERNADOS':'int', 'CURADOS':'int', 'NOTIFICADOS':'int', 'ISOLAMENTO':'int'})
        
        #Saving a new csv file
        #self.covid_data.to_csv('covid_data.csv', index=False)
        
        return self.covid_data
        '''
        #Print dataset information
        print(covid_data)
        print(covid_data.dtypes)
        print(covid_data)
        print("\nDataset information:")
        print(covid_data.info())
        print("\nMissing data information:")
        print(covid_data.isna().sum())
        '''  

    def webScraping(self):
        #WebScraping of data SESAEU/PAU_DOS_FERROS_COVID-19
        url = 'https://paudosferros.rn.gov.br/relatorio.php?id=24&rel=#'
        html = requests.get(url).content
        df_list = pd.read_html(html)
        self.df = df_list[-1]
        print(self.df)
        #df.to_csv('data.csv', index=False)
        return self.df
        

def makeplot(col_y):
	
	plt.style.use('dark_background')
	
	# make data
	x = np.arange(len(col_y))
	max_value = max(col_y)+4
	y = col_y
	
	# plot
	fig, ax = plt.subplots()
	
	ax.plot(x, y, linewidth=2.0)
	ax.set(xlim=(0, len(y)), xticks=np.arange(0, len(y), 5),
			ylim=(0, max_value), yticks=np.arange(0, max_value, 5))
	
	plt.show()

"Herança"
class SearchYear_Month(Data):
    def __init__(self, dataset):
        super().__init__(dataset)
        
    def buscaAno(self,anoInicial, anoFinal, selCol):
        
        inicio = f'{anoInicial}-01-01'
        final = f'{anoFinal}-31-12'
        #Busca por Ano
        selecao = (super().get_dataset()['DATA HORA']  >= inicio) & (super().get_dataset()['DATA HORA']  <= final)
        #print(selecao)
        """  df_filtrado = self.__dataset[selecao].reset_index()
        print(df_filtrado) """
        
    def buscaMes(self):
        pass

class Predict:
    def __init__(self, y, x=None) -> None:
        self.__y = y
        self.__x = x
        
        if self.__x == None:
            self.__x = np.arange(0,len(self.__y))

    def vizualicao(self):
        #print(self.__y)
        print(len(self.__x),len(self.__y))
        plt.plot(self.__y, '-m')
        plt.show()

    def fit(self, degree):
        self.__x = np.array(self.__x).reshape(-1,1)
        self.__y = np.array(self.__y).reshape(-1,1)
        self.__polyFeat = PolynomialFeatures(degree=degree)
        x = self.__polyFeat.fit_transform(self.__x)

        "TRAINING DATA"
        self.__model = linear_model.LinearRegression()
        self.__model.fit(x,self.__y)
        accuracy = self.__model.score(x,self.__y)

        print('Accuracy > ', round(accuracy*100,3), "%")
        
        print(len(self.__x),len(self.__y))
        plt.plot(self.__y, '-m')
        y0 = self.__model.predict(x)
        plt.plot(y0, '--b')
        plt.show()

    def prediction(self, num):
        print("PREDICTION")
        up_after = 1

        print(f'Prediction - Cases after {up_after}: ', end='')
        print(round(int(self.__model.predict(self.__polyFeat.fit_transform([[len(self.__y)+up_after]])))))
        
if __name__=='__main__':
    "Aqui voce mudar o path pra o data surjo kkkkk"
    lim = DataProcessing()
    dadosLimpo = lim.dataProcessing()

    #data = Data(dadosLimpo)
    #print(data.get_confirmados())
    
    #busca = SearchYear_Month(dadosLimpo)
    #busca.buscaAno(2019, 2020, 1)

    #tr = Predict(data.get_confirmados()[0:-2])
    #tr.vizualicao()
    #tr.fit(8)
