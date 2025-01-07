# TMDB Flask Application

## Project Overview
This project is a Flask-based web application that integrates with the TMDB (The Movie Database) API to fetch and display movie-related data. It provides custom APIs to access popular, top-rated, and upcoming movies, as well as a search functionality to find movies by title. The application is designed for ease of use and scalability, with options for local deployment and optional cloud hosting.

---

## How to Run the Application Locally

### Prerequisites
- Python 3.7 or higher installed on your system.
- An active TMDB API key (see "How to Generate an API Key" below).
- A code editor (e.g., VS Code) and a terminal.

### Steps

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/Godwingodu12/TMDB-Flask-App-url>
   cd TMDB-Flask-App
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   ```
   Activate the virtual environment:
   - **Windows**: `env\Scripts\activate`
   - **Mac/Linux**: `source env/bin/activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the API Key**
   - Create a `.env` file in the project root directory.
   - Add your TMDB API key:
     ```
     TMDB_API_KEY=your_api_key_here
     ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000/`.

---

## How to Install Dependencies Using pip

If you need to install dependencies manually, run:
```bash
pip install Flask requests python-dotenv
```
After installing, save them to `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## API Endpoints with Sample Requests and Responses

### 1. **Get Popular Movies**
- **Endpoint**: `/api/movies/popular`
- **Method**: `GET`
- **Sample Request**:
  ```bash
  curl http://127.0.0.1:5000/api/movies/popular
  ```
- **Sample Response**:
  ```json
  {
      "results": [
          {
              "title": "Movie Title",
              "release_date": "2025-01-01",
              "overview": "A short description."
          },
  
      ]
  }
  ```

### 2. **Get Top-Rated Movies**
- **Endpoint**: `/api/movies/top-rated`
- **Method**: `GET`
- **Sample Request**:
  ```bash
  curl http://127.0.0.1:5000/api/movies/top-rated
  ```


### 3. **Get Upcoming Movies**
- **Endpoint**: `/api/movies/upcoming`
- **Method**: `GET`
- **Sample Request**:
  ```bash
  curl http://127.0.0.1:5000/api/movies/upcoming
  ``

### 4. **Search Movies by Title**
- **Endpoint**: `/api/movies/search`
- **Method**: `GET`
- **Query Parameter**: `query` (string)
- **Sample Request**:
  ```bash
  curl "http://127.0.0.1:5000/api/movies/search?query=inception"
  ```
- **Sample Response**:
  ```json
  {
      "results": [
          {
              "title": "Inception",
              "release_date": "2010-07-16",
              "overview": "A mind-bending thriller."
          },
          
      ]
  }
  ```

---


## How to Generate an API Key and Configure It in the Project

### Steps to Generate an API Key
1. Go to the [TMDB Developer Portal](https://developer.themoviedb.org/reference/intro/getting-started).
2. Sign up for an account and verify your email.
3. Log in and navigate to the API section.
4. Generate a new API key.

### Steps to Configure the API Key
1. Create a `.env` file in the project directory.
2. Add the following line:
   ```
   TMDB_API_KEY=your_api_key_here
   ```

---

This README provides all the necessary details to understand, set up, and run the TMDB Flask application. If you have any questions or face issues, feel free to reach out!



