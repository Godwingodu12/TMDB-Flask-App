from flask import Flask, jsonify, render_template, request
import requests

# Create Flask app
app = Flask(__name__)

# API Key and configuration
API_KEY = 'cbae3dccd2886953746d7a003d78e703'
LANGUAGE = 'en-US'
BASE_URL = 'https://api.themoviedb.org/3'

@app.route('/')
def index():
    # Fetch popular movies from TMDB API
    response = requests.get(f"{BASE_URL}/movie/popular", params={'api_key': API_KEY, 'language': LANGUAGE})
    if response.status_code == 200:
        movies_data = response.json()  # Parse JSON response
        return jsonify(movies_data)  # Return JSON data as Flask response
    else:
        return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})

# Fetch top-rated movies
@app.route('/api/movies/top-rated', methods=['GET'])
def get_top_rated_movies():
    try:
        response = requests.get(f"{BASE_URL}/movie/top_rated", params={'api_key': API_KEY, 'language': LANGUAGE})
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Fetch upcoming movies
@app.route('/api/movies/upcoming', methods=['GET'])
def get_upcoming_movies():
    try:
        response = requests.get(f"{BASE_URL}/movie/upcoming", params={'api_key': API_KEY, 'language': LANGUAGE})
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Search for movies
@app.route('/api/movies/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '')  # Get the search query from the URL
    try:
        response = requests.get(f"{BASE_URL}/search/movie", params={'api_key': API_KEY, 'query': query, 'language': LANGUAGE})
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Fetch movie details by movie ID
@app.route('/api/movie/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    try:
        response = requests.get(f"{BASE_URL}/movie/{movie_id}", params={'api_key': API_KEY, 'language': LANGUAGE})
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to fetch data", "status_code": response.status_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Render the home page
@app.route('/home')
def home():
    return render_template('index.html')  # You can create a template for the homepage if needed

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
