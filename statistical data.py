# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1haZ1mVCC7i5-5NmKSSkzZ4BOyrIKasto
"""

import pandas as pd

# Sample DataFrame (including 'id' and 'Unnamed: 0' columns for demonstration)
data = {
    'Unnamed: 0': [0, 1, 2],
    'id': [101, 102, 103],
    'Age': [25, 30, 35],
    'Salary': [50000.0, 60000.0, 70000.0],
    'Is_Manager': [False, True, False]
}

df = pd.DataFrame(data)

# Drop 'id' and 'Unnamed: 0' columns
df.drop(['id', 'Unnamed: 0'], axis=1, inplace=True)

# Display statistical summary
print(df.describe())