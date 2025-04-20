-- Insert a new movie
CREATE OR REPLACE FUNCTION insert_movie(title VARCHAR, genre VARCHAR, release_year INT) RETURNS VOID AS $$
BEGIN
    INSERT INTO movies_movie (title, genre, release_year) VALUES (title, genre, release_year);
END;
$$ LANGUAGE plpgsql;

-- Get all movies
CREATE OR REPLACE FUNCTION get_movies() RETURNS TABLE(id INT, title VARCHAR, genre VARCHAR, release_year INT) AS $$
BEGIN
    RETURN QUERY SELECT id, title, genre, release_year FROM movies_movie;
END;
$$ LANGUAGE plpgsql;

-- Update a movie
CREATE OR REPLACE FUNCTION update_movie(movie_id INT, title VARCHAR, genre VARCHAR, release_year INT) RETURNS VOID AS $$
BEGIN
    UPDATE movies_movie SET title = title, genre = genre, release_year = release_year WHERE id = movie_id;
END;
$$ LANGUAGE plpgsql;

-- Delete a movie
CREATE OR REPLACE FUNCTION delete_movie(movie_id INT) RETURNS VOID AS $$
BEGIN
    DELETE FROM movies_movie WHERE id = movie_id;
END;
$$ LANGUAGE plpgsql;

-- Get a movie by ID
CREATE OR REPLACE FUNCTION get_movie_by_id(movie_id INT) RETURNS TABLE(id INT, title VARCHAR, genre VARCHAR, release_year INT) AS $$
BEGIN
    RETURN QUERY SELECT id, title, genre, release_year FROM movies_movie WHERE id = movie_id;
END;
$$ LANGUAGE plpgsql;

-- Get all ratings
CREATE OR REPLACE FUNCTION get_ratings() RETURNS TABLE(id INT, user_id INT, movie_id INT, score INT) AS $$
BEGIN
    RETURN QUERY SELECT id, user_id, movie_id, score FROM movies_rating;
END;
$$ LANGUAGE plpgsql;

-- Insert a new rating
CREATE OR REPLACE FUNCTION insert_rating(user_id INT, movie_id INT, score INT) RETURNS VOID AS $$
BEGIN
    INSERT INTO movies_rating (user_id, movie_id, score) VALUES (user_id, movie_id, score);
END;
$$ LANGUAGE plpgsql;

-- Get all watchlist entries
CREATE OR REPLACE FUNCTION get_watchlist() RETURNS TABLE(id INT, user_id INT, movie_id INT, watched BOOLEAN) AS $$
BEGIN
    RETURN QUERY SELECT id, user_id, movie_id, watched FROM movies_watchlist;
END;
$$ LANGUAGE plpgsql;

-- Insert a new watchlist entry
CREATE OR REPLACE FUNCTION insert_watchlist(user_id INT, movie_id INT, watched BOOLEAN) RETURNS VOID AS $$
BEGIN
    INSERT INTO movies_watchlist (user_id, movie_id, watched) VALUES (user_id, movie_id, watched);
END;
$$ LANGUAGE plpgsql;