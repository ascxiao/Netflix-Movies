import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sp

# Load dataset
st.title("Netflix Data Dashboard")
st.sidebar.title("Navigation")
netflix = pd.read_csv('netflix.csv')

# Ensure no null values
netflix = netflix.dropna(subset=['release_year', 'user_rating_score'])

# Assign variables
release_year = netflix['release_year']
user_rating_score = netflix['user_rating_score']

# Sidebar options
options = st.sidebar.radio("Choose a Visualization", [
    "Scatter Plot with Trendline",
    "Average Ratings by Decade",
    "Ratings by Rating Category",
    "Outliers in Ratings",
    "Correlation Heatmap"
])

# Scatter Plot with Trendline
if options == "Scatter Plot with Trendline":
    st.subheader("Scatter Plot: Netflix Ratings Over Time")
    slope, intercept, r_value, p_value, std_err = sp.linregress(release_year, user_rating_score)

    # Scatter plot
    fig, ax = plt.subplots()
    ax.scatter(release_year, user_rating_score, alpha=0.1, label="Ratings")

    # Trendline
    x_vals = pd.Series(range(release_year.min(), release_year.max() + 1))
    y_vals = slope * x_vals + intercept
    ax.plot(x_vals, y_vals, color='red', label="Trendline")
    ax.set_xlabel("Year")
    ax.set_ylabel("Rating")
    ax.set_title("Netflix Ratings Over Time")
    ax.legend()
    st.pyplot(fig)

# Average Ratings by Decade
if options == "Average Ratings by Decade":
    st.subheader("Average Netflix Ratings by Decade")
    netflix['decade'] = (netflix['release_year'] // 10) * 10
    avg_ratings = netflix.groupby('decade')['user_rating_score'].mean()

    # Bar chart
    fig, ax = plt.subplots()
    avg_ratings.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_xlabel("Decade")
    ax.set_ylabel("Average Rating")
    ax.set_title("Average Netflix Ratings by Decade")
    st.pyplot(fig)

# Ratings by Rating Category
if options == "Ratings by Rating Category":
    st.subheader("Average Netflix Ratings by Rating Category")
    netflix_na = netflix.dropna()
    genres = netflix_na.groupby('rating')['user_rating_score'].mean().sort_values()

    # Horizontal bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    genres.plot(kind='barh', color='lightblue', ax=ax)
    ax.set_xlabel("Average Rating")
    ax.set_ylabel("Rating Category")
    ax.set_title("Average Netflix Ratings by Rating Category")
    st.pyplot(fig)

# Outliers in Ratings
if options == "Outliers in Ratings":
    st.subheader("Outliers in Netflix Ratings Over Time")
    outliers = netflix[(netflix['user_rating_score'] > netflix['user_rating_score'].quantile(0.95)) |
                       (netflix['user_rating_score'] < netflix['user_rating_score'].quantile(0.05))]

    # Scatter plot with outliers
    fig, ax = plt.subplots()
    ax.scatter(netflix['release_year'], netflix['user_rating_score'], alpha=0.5, label="Ratings")
    ax.scatter(outliers['release_year'], outliers['user_rating_score'], color='red', label='Outliers')
    ax.set_xlabel("Year")
    ax.set_ylabel("Rating")
    ax.set_title("Netflix Ratings Over Time with Outliers")
    ax.legend()
    st.pyplot(fig)

# Correlation Heatmap
if options == "Correlation Heatmap":
    st.subheader("Correlation Between Features")
    correlation = netflix[['release_year', 'user_rating_score']].corr()

    # Correlation heatmap
    fig, ax = plt.subplots()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)
    st.write("Correlation Matrix:")
    st.write(correlation)
