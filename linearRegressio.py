import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dado = pd.read_csv("C:\\Users\\talis\\Desktop\\Projeto POO\\dadosCovid.csv")
dado.drop(['Unnamed: 0', 'DATA HORA'], axis=1, inplace=True)

# Removendo a ultima linha - Informação inrelevante
dado.drop(dado.index[-1], inplace=True)

# Tranformando os dados de object to int64
for i in dado.columns:
  if i != "DATA HORA":
    dado[f'{i}'] = pd.to_numeric(dado[f'{i}'])

X1 = []
def laco(total,i=0):
    if i == total:
        pass
    else:
        X1.append(i)
        laco(total,i+1)
    
laco(len(dado['CONFIRMADOS']))
x = np.array(X1)
y = []
for i in range(len(dado['CONFIRMADOS'])-1,-1,-1):
    y.append(dado['CONFIRMADOS'][i])
y = np.array(y)

print(x)
print(y)

plt.scatter(x,y)
plt.title("Grafico Linear")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

size  = dado["CONFIRMADOS"].count()
a,b = np.random.rand()*10,np.random.rand()*10
passo = 0.1

"Normalizando os dados"
x = np.linspace(-1,1,size)

#y = (dado['CONFIRMADOS'])
print(y.max())
y = y/max(y)

def imprimirGrafico(x,y,a,b):
    plt.scatter(x,y)
    plt.plot(x,a*x+b,"-",color='red')
    plt.grid(True)
    plt.pause(0.10)
    plt.cla()
    #plt.show()
    
for epoca in range(0,50):
    e = 0
    for _ in range(0,len(x)):
        i = int(np.random.rand()*dado['CONFIRMADOS'].count())
        e = y[i] - (a * x[i] + b)

        dj = (e**2)*(-x[i])
        dja = e*(-x[i])
        djb = -e
        a = a - passo * dja
        b = b - passo * djb
    
    imprimirGrafico(x,y,a,b)
    print("A >: ",a, "B >: ",b,"E >: ",e)