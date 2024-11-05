# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:34:15 2019

@author: ikulikov
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rc
import numpy as np
import matplotlib as mpl

mpl.font_manager._rebuild()
mpl.rc('font', family='serif', serif='Linguistics Pro') # Utopia LaTeX font with greek letters
mpl.rc('text', usetex=False)
mpl.rc('mathtext', fontset='custom', rm='Linguistics Pro', it='Linguistics Pro:italic', bf='Linguistics Pro:bold')

data = pd.read_csv('data.txt', sep=",", header=None,parse_dates=[5])
data.columns = ["Name","N_Z",'N','Z','A','half_life','unknown', 'year', 'mode']
yr=2016
data['year'].fillna(2020, inplace=True)
data['year'].astype(int)
data['mode'].fillna('XXX', inplace=True)
fig, (ax) = plt.subplots(1,1,figsize=(6,4))
#ax.set_ylim(0,180)
#ax.set_xlim(0,120)
#ax.scatter(data[data['year'] < yr]["N"], data[data['year'] < yr]["Z"], c='red')

scatter1=ax.scatter(data[(data['mode'].str.contains('B+',regex=False)) & (data['year'] < yr)]["N"], data[(data['mode'].str.contains('B+',regex=False)) & (data['year'] < yr)]["Z"], c='#F19997',s=0.55, marker='s')
scatter2=ax.scatter(data[(data['mode'].str.contains('p',regex=False)) & (data['year'] < yr)]["N"], data[(data['mode'].str.contains('p',regex=False)) & (data['year'] < yr)]["Z"], c='#F5C14C',s=0.55, marker='s')
scatter4=ax.scatter(data[(data['mode'].str.contains('n',regex=False)) & (data['year'] < yr)]["N"], data[(data['mode'].str.contains('n',regex=False)) & (data['year'] < yr)]["Z"], c='#80C9F1',s=0.55, marker='s')
scatter3=ax.scatter(data[(data['mode'].str.contains('B-',regex=False)) & (data['year'] < yr)]["N"], data[(data['mode'].str.contains('B-',regex=False)) & (data['year'] < yr)]["Z"], c='#4BA5E6',s=0.55, marker='s')
scatter5=ax.scatter(data[(data['mode'].str.contains('A',regex=False)) & (data['year'] < yr)]["N"], data[(data['mode'].str.contains('A',regex=False)) & (data['year'] < yr)]["Z"], c='#F0F050',s=0.55, marker='s')
scatter6=ax.scatter(data[(data['mode'].str.contains('SF',regex=False)) & (data['year'] < yr)]["N"], data[(data['mode'].str.contains('SF',regex=False)) & (data['year'] < yr)]["Z"], c='#68D142',s=0.55, marker='s')
scatter7=ax.scatter(data[(data['half_life'] == 'stbl') & (data['year'] < yr)]["N"], data[(data['half_life'] == 'stbl') & (data['year'] < yr)]["Z"], c='k',s=0.55, marker='s')

ax.legend((scatter7,scatter1,scatter3,scatter2,scatter4,scatter5,scatter6),("stable",r"$\beta^+$",r"$\beta^-$","p","n",r"$\alpha$","SF"),scatterpoints=3,loc='lower right',ncol=3,fontsize=6)
ax.set_xlabel('Neutron Number $N$',fontsize=16)
ax.set_ylabel('Proton Number $Z$',fontsize=16)
ax.set_ylim(-1,120)
ax.set_xlim(-1,180)
plt.text(130, 28,yr,fontsize=14)
mx1=8
mx2=20
mx3=28
mx4=50
mx5=82
mx6=126
my1=8
my2=20
my3=28
my4=50
my5=82
plt.axvline(x=mx1,ymin=0.03,ymax=0.16,color='black',linestyle='--',linewidth=0.5)
plt.axvline(x=mx2,ymin=0.1,ymax=0.25,color='black',linestyle='--',linewidth=0.5)
plt.axvline(x=mx3,ymin=0.12,ymax=0.31,color='black',linestyle='--',linewidth=0.5)
plt.axvline(x=mx4,ymin=0.23,ymax=0.45,color='black',linestyle='--',linewidth=0.5)
plt.axvline(x=mx5,ymin=0.35,ymax=0.65,color='black',linestyle='--',linewidth=0.5)
plt.axvline(x=mx6,ymin=0.55,ymax=0.8,color='black',linestyle='--',linewidth=0.5)

plt.axhline(y=my1,xmin=0.03,xmax=0.14,color='black',linestyle='--',linewidth=0.5)
plt.axhline(y=my2,xmin=0.09,xmax=0.25,color='black',linestyle='--',linewidth=0.5)
plt.axhline(y=my3,xmin=0.14,xmax=0.31,color='black',linestyle='--',linewidth=0.5)
plt.axhline(y=my4,xmin=0.29,xmax=0.52,color='black',linestyle='--',linewidth=0.5)
plt.axhline(y=my5,xmin=0.53,xmax=0.75,color='black',linestyle='--',linewidth=0.5)

xticks=np.array([8, 20, 28,50,82,126])
ax.xaxis.set_ticks(xticks, minor=False)
yticks=np.array([8, 20, 28,50,82])
ax.yaxis.set_ticks(yticks, minor=False)
#ax2.set_ylim(0,180)
#ax2.set_xlim(0,120)
#data.to_csv('check.txt')
plt.savefig("nuclear_chart_{}.pdf".format(yr),  bbox_inches='tight')
plt.show()