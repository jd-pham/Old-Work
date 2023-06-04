import pandas as pd
import pathlib
import math

def compute_info_gain(col):
	print(col)
def compute_decision_order(df):
	
	compute_info_gain(df[0])

df1 = pd.read_excel('dataset.xlsx', sheet_name=0)
df2 = pd.read_excel('dataset.xlsx', sheet_name=1)
print(df1)
# print(df1.loc['Rain'])
# compute_decision_order(df1)