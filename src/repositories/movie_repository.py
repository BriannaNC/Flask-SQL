from src.models import movie, db
class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        Movie=movie.query.all()
        return Movie

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        
        Movie= movie.query.filter_by(movie_id = movie_id).first()
        return Movie

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        new_movie=movie(title=title,director=director,rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        Movie=movie.query.filter(movie.title.like(f"%{title}%")).all()
        return Movie


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
