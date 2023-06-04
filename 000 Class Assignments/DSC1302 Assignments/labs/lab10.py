import os
import pandas as pd


excel_tables = []
for table in os.listdir('lab10_data/'):
    excel_tables += [pd.read_excel(f'lab10_data/{table}')]


q1 = excel_tables[0]
q1 = q1.groupby('year', group_keys=True).apply(lambda x: x)
print(q1)
print('END OF Q1 -------------------------------------------------------')


print()
q2 = excel_tables[1].merge(excel_tables[2], how='outer', on=['Player_name', 'game 1', 'game 2', 'game 3'])
print(q2)
print('END OF Q2 -------------------------------------------------------')
