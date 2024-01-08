import pandas as pd
import random
import numpy as np
dataset = pd.read_csv('census.csv')

'''
    Digamos que queremos utilizar dessa população uma amostra de 100
    então pegamos o tamnho do dataset e dividiomos por 100
        32561 / 100 = 325
'''

variavel_aleatorio = len(dataset) // 100

# Geramos numero aleatorio entre 0 e o resultado acima

# para executarmos esse teste vamos definir o seed como 1 para sempre gerar o 
# mesmo número

random.seed(1)
random.randint(0, variavel_aleatorio)

# o resultado de 291 entamos é selecionado o primeiro elemento  que é 291
# nesse caso fariamos o seguinte 291 + 325 para pegar o proximo elemento
# da nossa amostra, para não termos que fazer um loop de 100 vezes para para o 
# proximo numero utilizamos uma função do numpy

teste = np.arange(68, len(dataset), step = 325 )

# com isso temos os 100 numeros dentro do range da nossa amostragem sistemática

# vamos criar uma função que faz esse cálculo 

def amostragem_sistematica(dataset,amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step = intervalo )
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica

df_amostra_sistematica = amostragem_sistematica(dataset, 30)