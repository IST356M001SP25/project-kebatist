import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load the cleaned CSV data
    return pd.read_csv(file_path)

def plot_data(df):
    # Example plot: Distribution of Ratings
    plt.figure(figsize=(10,6))
    sns.histplot(df['rating'], bins=20, kde=True, color='blue')
    plt.title('Distribution of IMDB Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    st.pyplot()

def show_dashboard(df):
    # Display basic info and the first few rows
    st.title("IMDB Top 250 Movies Dashboard")
    st.write("This dashboard shows the top 250 movies from IMDB with ratings and other details.")

    # Display data preview
    st.subheader('Data Preview')
    st.write(df.head())

    # Show a plot of the distribution of ratings
    st.subheader('Rating Distribution')
    plot_data(df)

    # Show other insights (for example, average rating by genre)
    st.subheader('Average Rating by Genre')
    avg_rating_by_genre = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
    st.write(avg_rating_by_genre)

# Run the app
if __name__ == "__main__":
    # Path to the transformed CSV file
    transformed_csv_path = r"C:\Users\batis\IST 356 Program Tech\VS Code\project-kebatist\data\IMDB Top 250 Transformed.csv"
    df = load_data(transformed_csv_path)
    show_dashboard(df)
