import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

df = pd.read_csv('multiseries.csv')

t = df['LOAD_DTE'] = pd.to_datetime(df['LOAD_DTE'])
c = df['REF_CNT']
s = df['STDV']
m = df['MEAN']
l = df['LCL']
u = df['UCL']


possibilities = [   u'_classic_test',
                    u'bmh',
                    u'classic',
                    u'dark_background',
                    u'fivethirtyeight',
                    u'ggplot',
                    u'grayscale',
                    u'seaborn',
                    u'seaborn-bright',
                    u'seaborn-colorblind',
                    u'seaborn-dark',
                    u'seaborn-darkgrid',
                    u'seaborn-dark-palette',
                    u'seaborn-deep',
                    u'seaborn-muted',
                    u'seaborn-notebook',
                    u'seaborn-paper',
                    u'seaborn-pastel',
                    u'seaborn-poster',
                    u'seaborn-talk',
                    u'seaborn-ticks',
                    u'seaborn-white',
                    u'seaborn-whitegrid']


x = random.choice([x for x in possibilities])

x = 'grayscale'
plt.style.use(x)

tick_spacing = 1

fig, ax = plt.subplots(figsize=(8,5.5))

ax.plot(t, c, marker='o', markerfacecolor='blue', markersize=3, color='skyblue', linewidth=2, label='Referal Count')
ax.plot(t, m, color='b', label='Mean', linestyle='dashed')
ax.plot(t, l, marker='', color='red', linewidth=2, label='Lower Control Limit')
ax.plot(t, u, marker='', color='red', linewidth=2, label='Upper Control Limit')
ax.set_title(x)


plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

