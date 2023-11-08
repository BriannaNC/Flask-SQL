# TODO - Create SQLAlchemy DB and Movie model

from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class movie(db.Model):
    movie_id= db.Column(db.Integer,primary_key=True)
    title= db.Column(db.String(255),nullable=False)
    director= db.Column(db.String(255),nullable=False)
    rating= db.Column(db.Integer,nullable=False)

    def __init__(self,title, director, rating):
        self.title=title
        self.director=director
        self.rating=rating
