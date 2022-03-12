import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os import system
import platform

"Aqui verifica o sistema operacional e aplica a função limpar ao terminal"
if platform.system() == 'Windows':
    system("cls")
else:
    system("clear")

url = 'https://paudosferros.rn.gov.br/relatorio.php?id=24&rel=#'

data = pd.read_html(url)
print(data)
"Transformando em um arquivo CSV"
""" df = pd.DataFrame(data[0])

df.to_csv('dadosCovid.csv')

data = pd.read_csv("C:\\Users\\talis\\Desktop\\Projeto POO\\dadosCovid.csv")
data.drop(['Unnamed: 0'], axis=1, inplace=True)
print(data.columns) """



'Informações da base de dados'
#print(data[0].iloc[-1])

month = input('Informe o mes >: ')
year = input('Informe o ano >: ')

if '0' not in month and len(month) == 1:
    month = str(0) + month

result = data[data['DATA HORA'].str.contains(f'/{month}/{year}')]

#result.drop(['DATA HORA'],axis=1, inplace=True)
#print(result.astype(int).sum())

# Plotando os Gráficos de Linha
plt.bar(result['CONFIRMADOS'], result['DATA HORA'])
plt.show()