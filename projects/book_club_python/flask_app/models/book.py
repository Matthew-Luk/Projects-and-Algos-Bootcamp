from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Book:
    db = "book_club"
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books(title,description) VALUES(%(title)s,%(description)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for row in results:
            books.append(cls(row))
        return books