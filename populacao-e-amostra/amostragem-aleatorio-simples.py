import pandas as pd
import random
import numpy as np


dataset = pd.read_csv('census.csv')

df_amostra_aleatoria_simples = dataset.sample(n=100)

def amostragem_aleatorio_simples(dataset, amostras):
    return dataset.sample(n = amostras)

df_amostra_result_function = amostragem_aleatorio_simples(dataset, 10)
