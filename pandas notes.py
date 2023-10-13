#import web_scraper #commented out for dev purposes, uncomment when doing full testing
import pandas as pd
import numpy as np

movie_df=pd.read_csv(r"D:\GitHub\data vis project\animated_movies.csv")
#print(movie_df.info())
print(movie_df[movie_df['Year'] > 2015])

specific_movies=['Coco','Frozen','Moana']
print(movie_df[movie_df['Title'].isin(specific_movies)])

print(movie_df[movie_df['Title'].str.contains('Frozen')])


movie_df2 = movie_df.set_index('Title')
print(movie_df2.filter(items= ['Title','Worldwide gross'], axis = 1))
print(movie_df2.filter(like= 'Frozen', axis = 0))
print(movie_df2.loc['Frozen'])
print(movie_df2.iloc[10])

print(movie_df[movie_df['Year'] > 2015].sort_values(by=['Year','Worldwide gross'],ascending=False))