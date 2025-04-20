# Movie Recommendation Service

## Overview
This project is a RESTful API application that serves as a movie recommendation service. It allows users to rate movies, and the system generates personalized movie recommendations based on user preferences and watch history.

## Features
- User Management: Registration, authentication (using JWT), and profile management.
- Movie Management: Create, read, update, and delete movie entries. Search and filter movies based on various criteria.
- User Interaction: Rate movies, add movies to watchlist, and mark movies as watched.
- Recommendation Engine: Generate personalized movie recommendations using collaborative and content-based filtering.
- Asynchronous Tasks: Update recommendations, process new ratings, send email notifications, and import movie data from an external API.

## Technical Requirements
- **Backend:** Django 4.2+ and Django REST Framework
- **Database:** PostgreSQL with stored procedures for CRUD operations
- **Asynchronous Tasks:** Celery with Redis as a broker
- **Testing:** Comprehensive unit tests using pytest
- **Containerization:** Docker and Docker Compose

## Setup Instructions

### Prerequisites
- Python 3.9+
- Docker and Docker Compose
- PostgreSQL
- Redis

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/r4hulch0udhary/movie_recommendation.git
   cd movie_recommendation
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Create a PostgreSQL database and user.
   - Run the `create_procedures.sql` file to set up stored procedures.

5. **Configure environment variables:**
   - Create a `.env` file based on `env.example` and set the necessary environment variables.

6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Start the application:**
   ```bash
   docker-compose up --build
   ```

## Testing

### Running Tests
- **Unit Tests:**
  ```bash
  python manage.py test
  ```

## API Documentation
- Access the Swagger UI at `http://localhost:8000/swagger/` for API documentation.

## License
- This project is licensed under the MIT License.
