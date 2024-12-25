import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

netflix = pd.read_csv('netflix.csv')

plt.scatter(netflix['release_year'], netflix['user_rating_score'])
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title ("Netflix Ratings Over Time")

plt.show()