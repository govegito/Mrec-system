# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:39:26 2019

@author: jayesh
"""

import numpy as np
import pandas as pd

df=pd.read_csv('ratings.csv')

movie_titles = pd.read_csv("movies.csv")

df=pd.merge(df,movie_titles,on='movieId')

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
%matplotlib inline

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

#plt.figure(figsize=(10,4))
#ratings['num of ratings'].hist(bins=70)

moviemat = df.pivot_table(index='userId',columns='title',values='rating')


ratings.sort_values('num of ratings',ascending=False).head()

forestgump_user_ratings = moviemat['Forrest Gump (1994)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

similar_to_forestgump = moviemat.corrwith(forestgump_user_ratings)

corr_fg=pd.DataFrame(similar_to_forestgump,columns=['Correlation'])
corr_fg.dropna(inplace=True)

corr_fg.sort_values('Correlation',ascending=False).head()
corr_fg = corr_fg.join(ratings['num of ratings'])


corr_fg[corr_fg['num of ratings']>100].sort_values('Correlation',ascending=False).head()
