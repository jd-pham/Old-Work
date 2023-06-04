# %%
import pandas as pd

# %%
df = pd.read_csv('calm_20_5_2020.csv', parse_dates=True, encoding='latin1')

df_rt = df[df['isRetweet'] == True]
df_rt.groupby('screenName').sum().sort_values(by='retweetCount', ascending=False)
print(df_rt)


