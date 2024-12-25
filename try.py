import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as sp

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
plt.scatter(release_year , user_rating_score, alpha = 0.1)

#Trendline
x_vals = pd.Series(range(release_year.min(), release_year.max() + 1))
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color = 'red', label = "Trendline")

#Visualize
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title ("Netflix Ratings Over Time")
plt.legend()

plt.show()