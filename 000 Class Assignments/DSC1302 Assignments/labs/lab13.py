import pandas as pd
import os
from matplotlib import pyplot as plt


folder_path = f'{os.getcwd()}\\LAB_ Broadway show scatter plot\\broadway_jul_2000.csv'
df1 = pd.read_csv(folder_path)
df1['Size'] = df1['Gross Potential'] / 2
print(df1)

plt.scatter(x=df1['Capacity'], y=df1['Gross Potential'], 
            marker='x',
            c='orange',
            s=df1['Size'])



decem = pd.read_csv(f'LAB_ Broadway show multiple plots\\broadway_dec_2002.csv')
july = pd.read_csv(f'LAB_ Broadway show multiple plots\\broadway_jul_2002.csv')

print(decem)
print(july)


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,10))
fig.suptitle('Capacity vs Gross Potential')


axes[0].scatter(july['Gross Potential'], july['Capacity']) 
axes[1].scatter(decem['Gross Potential'], decem['Capacity'])