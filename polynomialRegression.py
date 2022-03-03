import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model 
from sklearn.preprocessing import PolynomialFeatures
#import os
#os.system('cls')

"Aqui o path dos dados"
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
    
laco(len(dado['CONFIRMADOS'])-1)

y = []
for i in range(len(dado['CONFIRMADOS'])-1,1,-1):
    y.append(dado['CONFIRMADOS'][i])

print(y)
x = np.array(x).reshape(-1,1)
y = np.array(y).reshape(-1,1)
#print(len(x),len(y))
plt.plot(y, '-m')
#plt.show()

polyFeat = PolynomialFeatures(degree=10)
x = polyFeat.fit_transform(x)

"TRAINING DATA"
model = linear_model.LinearRegression()
model.fit(x,y)
accuracy = model.score(x,y)
print('Accuracy > ', round(accuracy*100,3), "%")
y0 = model.predict(x)
plt.plot(y0, '--b')
plt.show()

print("PREDICTION")
up_after = 1

print(dado['CONFIRMADOS'].sum())
print(f'Prediction - Cases after {up_after}: ', end='')
print(round(int(model.predict(polyFeat.fit_transform([[len(x)+up_after]])))))
print(dado['CONFIRMADOS'].sum())