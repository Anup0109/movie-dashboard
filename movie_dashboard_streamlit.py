import streamlit as st
import pandas as pd
import plotly.express as px

# Generate a sample dataset
movies = [
    {"Title": "Inception", "Genre": "Sci-Fi", "Platform": "Netflix", "Revenue": 500000000, "Rating": 8.8},
    {"Title": "The Godfather", "Genre": "Drama", "Platform": "Amazon Prime", "Revenue": 300000000, "Rating": 9.2},
    {"Title": "Avengers: Endgame", "Genre": "Action", "Platform": "Disney+", "Revenue": 2797800564, "Rating": 8.4},
    {"Title": "Parasite", "Genre": "Thriller", "Platform": "Hulu", "Revenue": 258000000, "Rating": 8.6},
    {"Title": "Interstellar", "Genre": "Sci-Fi", "Platform": "HBO Max", "Revenue": 701729206, "Rating": 8.7},
]

# Create a DataFrame
df = pd.DataFrame(movies)

# Create a treemap visualization
fig = px.treemap(df, path=["Platform", "Genre", "Title"], values="Revenue", color="Rating",
                 title="Movie Dashboard: Revenue Breakdown")

# Streamlit layout
st.title("Movie Dashboard")
st.plotly_chart(fig)

# Add interactivity with filters
st.sidebar.header("Filters")
selected_platform = st.sidebar.multiselect("Select Platform", df["Platform"].unique(), default=df["Platform"].unique())
selected_genre = st.sidebar.multiselect("Select Genre", df["Genre"].unique(), default=df["Genre"].unique())

# Filter DataFrame based on user selections
filtered_df = df[(df["Platform"].isin(selected_platform)) & (df["Genre"].isin(selected_genre))]

# Update visualization with filtered data
if not filtered_df.empty:
    filtered_fig = px.treemap(filtered_df, path=["Platform", "Genre", "Title"], values="Revenue", color="Rating",
                              title="Filtered Movie Dashboard")
    st.plotly_chart(filtered_fig)
else:
    st.warning("No data matches the selected filters.")
