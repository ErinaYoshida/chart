# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 19:02:48 2021

@author: erina
"""

import pandas as pd
import matplotib.pyplot as plt

df = pd.read_excel("skill_check.xlsx", usecols=[1,2,4,5])
# usecolsで読み込む列を指定
print(df)