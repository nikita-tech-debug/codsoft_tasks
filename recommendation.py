movies = {
    "Avengers": ["Action", "Adventure", "Superhero"],
    "Iron Man": ["Action", "Adventure", "Superhero"],
    "Spider-Man": ["Action", "Adventure", "Superhero"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "Interstellar": ["Sci-Fi", "Adventure"],
    "Inception": ["Sci-Fi", "Action"]
}


def recommend(movie_name):
    if movie_name not in movies:
        print("Movie not found.")
        return

    selected_genres = set(movies[movie_name])

    recommendations = []

    for movie, genres in movies.items():

        if movie == movie_name:
            continue

        common_genres = selected_genres.intersection(genres)
        similarity = len(common_genres)

        if similarity > 0:
            recommendations.append((movie, similarity))

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n===== RECOMMENDATIONS =====")
    print("Based on:", movie_name)

    for movie, score in recommendations:
        print("-", movie)


print("===== MOVIE RECOMMENDATION SYSTEM =====")
print("Available movies:")

for movie in movies:
    print("-", movie)

movie = input("\nEnter your favorite movie: ")

recommend(movie)