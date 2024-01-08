# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:56:30 2024

@author: lucasg
"""

import pandas as pd
import numpy as np
import random 

dataset = pd.read_csv('census.csv')


def amostragem_agrupamento(dataset, numero_grupos):
  intervalo = len(dataset) / numero_grupos

  grupos = []
  id_grupo = 0
  contagem = 0
  for _ in dataset.iterrows():
    grupos.append(id_grupo)
    contagem += 1
    if contagem > intervalo:
      contagem = 0
      id_grupo += 1

  dataset['grupo'] = grupos
  random.seed(1)
  #grupo_selecionado = random.randint(0, numero_grupos)
  grupo_selecionado = random.randint(0, numero_grupos - 1) #Atualizado 16/10/2023
  return dataset[dataset['grupo'] == grupo_selecionado]


df_amotra_agrupamento = amostragem_agrupamento(dataset, 50)

print(df_amotra_agrupamento.head())
print(df_amotra_agrupamento.tail())