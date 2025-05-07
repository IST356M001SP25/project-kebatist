# code/dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import geopandas as gpd

# Load the transformed data (make sure the path matches the location of your cleaned CSV)
DATA_PATH = 'cache/clean_data.csv'
df = pd.read_csv(DATA_PATH)

# Streamlit page setup
st.set_page_config(page_title="Streaming Platform Diversity Analyzer", layout="wide")

# Sidebar filters
st.sidebar.header("Filters")

# Filter by genre
genre_filter = st.sidebar.multiselect(
    "Select Genre(s)", df['genre'].unique(), default=df['genre'].unique()
)

# Filter by year range
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_filter = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter by rating range
rating_filter = st.sidebar.slider("Select Rating Range", 1, 10, (1, 10))

# Apply filters to the dataframe
df_filtered = df[
    (df['genre'].apply(lambda x: any(genre in x for genre in genre_filter))) &
    (df['year'] >= year_filter[0]) & (df['year'] <= year_filter[1]) &
    (df['rating'] >= rating_filter[0]) & (df['rating'] <= rating_filter[1])
]

# Main dashboard title
st.title("Streaming Platform Diversity Analyzer")
st.write("Explore diversity in IMDb's Top 250 Movies and TV Shows")

# Show some of the filtered data
st.subheader(f"Filtered Data (Showing {len(df_filtered)} records)")
st.dataframe(df_filtered[['rank', 'name', 'year', 'rating', 'genre', 'certificate']])

# Visualizations

# 1. Distribution of Ratings
st.subheader("Distribution of Ratings")
fig_rating = sns.histplot(df_filtered['rating'], kde=True, color="blue")
st.pyplot(fig_rating.figure)

# 2. Count of Movies by Genre
st.subheader("Number of Movies by Genre")
genre_count = df_filtered['genre'].explode().value_counts()
fig_genre = genre_count.plot(kind='bar', color='green')
st.pyplot(fig_genre.figure)

# 3. Year vs. Rating (Scatter plot)
st.subheader("Year vs. Rating")
fig_year_rating = px.scatter(df_filtered, x='year', y='rating', color='genre', title="Year vs. Rating")
st.plotly_chart(fig_year_rating)

# 4. Boxplot of Ratings by Genre
st.subheader("Ratings Distribution by Genre")
fig_genre_rating_boxplot = sns.boxplot(x="genre", y="rating", data=df_filtered)
st.pyplot(fig_genre_rating_boxplot.figure)

# Optional: Geospatial plot (if you have country or location data)
# st.subheader("Map of Filming Locations")  
# gdf = gpd.read_file('path_to_shapefile')  # Uncomment if you want to use geospatial data
# st.map(gdf)

