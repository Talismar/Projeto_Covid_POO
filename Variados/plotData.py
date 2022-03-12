import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.system('cls')

dado = pd.read_csv("C:\\Users\\talis\\Desktop\\Projeto POO\\dadosCovid.csv")
dado.drop(['Unnamed: 0', 'DATA HORA'], axis=1, inplace=True)

# Removendo a ultima linha - Informação inrelevante
dado.drop(dado.index[-1], inplace=True)

# Tranformando os dados de object to int64
for i in dado.columns:
  if i != "DATA HORA":
    dado[f'{i}'] = pd.to_numeric(dado[f'{i}'])

x = []
def laco(total,i=1):
    if i == total:
        pass
    else:
        x.append(i)
        laco(total,i+1)
    
laco(len(dado['DESCARTADOS'])+1)

y = []
for j in ['SUSPEITOS','CONFIRMADOS','DESCARTADOS','ÓBITOS','INTERNADOS','CURADOS','NOTIFICADOS','ISOLAMENTO']:
    for i in range(len(dado[j])-1,-1,-1):
        y.append(dado[j][i])

    #x = np.array(x).reshape(-1,1)
    #y = np.array(y).reshape(-1,1)
    #print(len(x),len(y))
    plt.plot(y, '-m')
    plt.title(j)
    plt.pause(1)
    plt.cla()    
    y.clear()


print(dado['NOTIFICADOS'].isnull().sum())