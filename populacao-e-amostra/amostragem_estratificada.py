# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:00:41 2024

@author: lucasg
"""

import pandas as pd
import numpy as np
import random 
from sklearn.model_selection import StratifiedShuffleSplit

dataset = pd.read_csv('census.csv')