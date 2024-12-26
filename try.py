import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as sp
import seaborn as sns

#Load data
netflix = pd.read_csv('netflix.csv')

#Ensure no null values
netflix = netflix.dropna(subset=['release_year', 'user_rating_score'])

#Assign variables
release_year = netflix['release_year']
user_rating_score = netflix['user_rating_score']

#Perform linear regression
slope, intercept, r_value, p_value, std_err = sp.linregress(release_year, user_rating_score)

#Scatter plot to check correlation
netflix.plot(x = "release_year" ,y = "user_rating_score", kind = 'scatter', alpha = 0.1)

#Trendline
x_vals = pd.Series(range(release_year.min(), release_year.max() + 1))
y_vals = slope * x_vals + intercept
plt.plot(x_vals,y_vals,color = 'red', label = "Trendline")

#Visualize
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title ("Netflix Ratings Over Time")
plt.legend()
plt.show()

#Average ratings by decade
netflix['decade'] = (netflix['release_year'] // 10) * 10
avg_ratings = netflix.groupby('decade')['user_rating_score'].mean()

avg_ratings.plot(kind='bar', color='skyblue')
plt.xlabel("Decade")
plt.ylabel("Average Rating")
plt.title("Average Netflix Ratings by Decade")
plt.show()

#Comparing rating level
netflix_na = netflix.dropna()
genres = netflix_na.groupby('rating')['user_rating_score'].mean().sort_values()
genres.plot(kind = 'barh', figsize = (8,6), color = 'lightblue')
plt.xlabel("Rating")
plt.ylabel("Average Rating")
plt.title("Average Netflix Ratings by Rating Category")
plt.show()

outliers = netflix[(netflix['user_rating_score'] > netflix['user_rating_score'].quantile(0.95)) |
                   (netflix['user_rating_score'] < netflix['user_rating_score'].quantile(0.05))]

plt.scatter(netflix['release_year'], netflix['user_rating_score'], alpha=0.5)
plt.scatter(outliers['release_year'], outliers['user_rating_score'], color='red', label='Outliers')
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title("Netflix Ratings Over Time with Outliers")
plt.legend()
plt.show()

correlation = netflix[['release_year', 'user_rating_score']].corr()
print(correlation)

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Between Features")
plt.show()
