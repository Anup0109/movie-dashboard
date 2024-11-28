import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import random

# Generate the dataset (same as before)
titles = [
    "Inception", "Pulp Fiction", "Avengers: Endgame", "The Godfather", "Parasite", "Interstellar",
    "Joker", "Black Panther", "Titanic", "Shutter Island", "The Dark Knight", "The Matrix",
    "Fight Club", "Forrest Gump", "Gladiator", "The Lion King", "Toy Story", "Star Wars: A New Hope",
    "Harry Potter and the Sorcerer's Stone", "The Lord of the Rings: The Fellowship of the Ring",
    "The Avengers", "Frozen", "Finding Nemo", "The Shawshank Redemption", "The Social Network",
    "The Wolf of Wall Street", "Iron Man", "Spider-Man: No Way Home", "Avatar", "Coco", "Inside Out",
    "Up", "The Incredibles", "Ratatouille", "Brave", "Wall-E", "Doctor Strange", "Guardians of the Galaxy",
    "Thor: Ragnarok", "Black Widow", "Eternals", "The Batman", "Wonder Woman", "Captain America: Civil War",
    "Shazam!", "The Hunger Games", "Twilight", "The Twilight Saga: New Moon", "La La Land", "Dune"
]
genres = [
    "Sci-Fi, Action", "Crime, Drama", "Action, Adventure", "Drama, Thriller", "Comedy, Romance",
    "Animation, Family", "Fantasy, Adventure", "Horror, Mystery", "Biography, Drama", "Action, Fantasy"
]
directors = [
    "Christopher Nolan", "Quentin Tarantino", "Anthony Russo", "Bong Joon Ho", "Francis Ford Coppola",
    "Martin Scorsese", "Steven Spielberg", "James Cameron", "Taika Waititi", "Denis Villeneuve"
]
platforms = ["Netflix", "Hulu", "Disney+", "HBO Max", "Amazon Prime", "Apple TV+"]

# Generate random movie data
random.seed(42)
movies = []
for i, title in enumerate(titles):
    movie = {
        "Title": title,
        "Year": random.randint(1970, 2022),
        "Genre": random.choice(genres),
        "Director": random.choice(directors),
        "Language": random.choice(["English", "Korean", "French", "Spanish", "German"]),
        "Budget": random.randint(5000000, 300000000),
        "Revenue": random.randint(10000000, 3000000000),
        "IMDb Rating": round(random.uniform(6.0, 9.5), 1),
        "Audience Rating": round(random.uniform(6.0, 9.5), 1),
        "Awards": random.randint(0, 15),
        "Streaming Platform": random.choice(platforms)
    }
    movies.append(movie)

df = pd.DataFrame(movies)

# Create Dash app
app = dash.Dash(__name__)

# Treemap visualization
def create_treemap():
    return px.treemap(
        df,
        path=['Streaming Platform', 'Genre', 'Title'],
        values='Revenue',
        color='IMDb Rating',
        hover_data={'Revenue': True, 'Budget': True, 'IMDb Rating': True, 'Audience Rating': True},
        title="Treemap: Revenue by Platform, Genre, and Title (Colored by IMDb Rating)"
    )

# App layout
app.layout = html.Div([
    html.H1("Movie Dashboard", style={"textAlign": "center"}),
    dcc.Graph(figure=create_treemap())
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
