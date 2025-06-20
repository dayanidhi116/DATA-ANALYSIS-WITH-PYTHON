# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1haZ1mVCC7i5-5NmKSSkzZ4BOyrIKasto
"""

import pandas as pd

# Sample DataFrame with a 'floor' column
data = {
    'floor': [1, 2, 2, 3, 1, 4, 2, 1, 3, 4, 5, 2]
}

df = pd.DataFrame(data)

# Count the number of houses by floor and convert to DataFrame
floor_counts = df['floor'].value_counts().to_frame(name='count')

# Display the result
print(floor_counts)