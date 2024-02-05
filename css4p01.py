# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:06:21 2024

@author: nhlam
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("movie_dataset.csv")
print(df)
"""
     Rank                    Title  ... Revenue (Millions) Metascore
0       1  Guardians of the Galaxy  ...             333.13      76.0
1       2               Prometheus  ...             126.46      65.0
2       3                    Split  ...             138.12      62.0
3       4                     Sing  ...             270.32      59.0
4       5            Suicide Squad  ...             325.02      40.0
..    ...                      ...  ...                ...       ...
995   996     Secret in Their Eyes  ...                NaN      45.0
996   997          Hostel: Part II  ...              17.54      46.0
997   998   Step Up 2: The Streets  ...              58.01      50.0
998   999             Search Party  ...                NaN      22.0
999  1000               Nine Lives  ...              19.64      11.0

[1000 rows x 12 columns]
"""
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""
print(df.describe())
"""
 Rank         Year  ...  Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000

[8 rows x 7 columns]
"""
df = pd.read_csv("movie_dataset.csv")
pd.set_option('display.max_row',None)
print(df)

#replacing empty values 
x = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(x, inplace = True)


x = df["Metascore"].mean()
df["Metascore"].fillna(x, inplace = True)

print(df)

#removing space of column names 
#df.columns = df.columns.str.replace(" ", "")
#print(df)

#Highest rated
index_of_highest_rated_movie = df['Rating'].idxmax()
highest_rated_movie = df.loc[index_of_highest_rated_movie]
print("Details of the highest-rated movie:")
print(highest_rated_movie)
"""
Details of the highest-rated movie:
Rank                                                                 55
Title                                                   The Dark Knight
Genre                                                Action,Crime,Drama
Description           When the menace known as the Joker wreaks havo...
Director                                              Christopher Nolan
Actors                Christian Bale, Heath Ledger, Aaron Eckhart,Mi...
Year                                                               2008
Runtime (Minutes)                                                   152
Rating                                                              9.0
Votes                                                           1791916
Revenue (Millions)                                               533.32
Metascore                                                          82.0
Name: 54, dtype: object
"""

# Display the average revenue
average_revenue = df["Revenue (Millions)"].mean()
print("Average Revenue (Millions):", average_revenue)
"""
Average Revenue (Millions): 82.95637614678898
"""

# average revenue
filtered_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_2017 = filtered_movies['Revenue (Millions)'].mean()
print("Average Revenue (Millions) for movies released between 2015 and 2017:", average_revenue_2015_2017)
"""
Average Revenue (Millions) for movies released between 2015 and 2017: 68.06402328198025
"""

#movies released
movies_twenty_sixteen = df[df['Year'] == 2016]
count_twenty_sixteen = len(movies_twenty_sixteen)
print("Number of movies released in 2016:", count_twenty_sixteen)
"""
Number of movies released in 2016: 297
"""

#Movies dierected by Christoper 
movies_by_nolan = df[df['Director'] == 'Christopher Nolan']
count_movies_by_nolan = len(movies_by_nolan)
print("Number of movies directed by Christopher Nolan:", count_movies_by_nolan)
"""
Number of movies directed by Christopher Nolan: 5
"""

#movie rating 
movie_ratings = df[df['Rating'] >= 8.0]
count_movie_ratings = len(movie_ratings)
print("Number of movies that rate at 8.0:", count_movie_ratings)
"""
Number of movies that rate at 8.0: 78
"""

#median rating
median_rating_nolan = movies_by_nolan['Rating'].median()
print("Median Rating of movies directed by Christopher Nolan:", median_rating_nolan)
"""
Median Rating of movies directed by Christopher Nolan: 8.6
"""

#highest average rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()
print("Year with the highest average rating:", year_highest_average_rating)
print("Highest average rating:", highest_average_rating)
"""
Year with the highest average rating: 2007
Highest average rating: 7.133962264150944
"""

#percentage increase
movies_2006_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]
count_movies_2006 = len(df[df['Year'] == 2006])
count_movies_2016 = len(df[df['Year'] == 2016])
percentage_increase = ((count_movies_2016 - count_movies_2006) / count_movies_2006) * 100
print("Number of movies in 2006:", count_movies_2006)
print("Number of movies in 2016:", count_movies_2016)
print(f"Percentage increase: {percentage_increase:.2f}%")
"""
Percentage increase: 575.00%
"""

# common actor
all_actors = ', '.join(df['Actors'].astype(str))
list_of_actors = all_actors.split(', ')
actor_counter = Counter(list_of_actors)
most_common_actor = actor_counter.most_common(1)[0][0]
print("Most common actor:", most_common_actor)
print("Number of occurrences:", actor_counter[most_common_actor])
"""
Most common actor: Mark Wahlberg
"""

#unique genres 
num_unique_genres = df['Genre'].str.split(',').explode().str.strip().nunique()
print("Number of unique genres:", num_unique_genres)
"""
Number of unique genres: 20
"""

#correlation
plt.xlabel('Rating')
plt.ylabel('Revenue (Millions)')
plt.title('Scatter Plot: Rating vs. Revenue')
plt.scatter(df['Rating'], df['Revenue (Millions)'])
plt.show()

df.to_csv("movies.csv")