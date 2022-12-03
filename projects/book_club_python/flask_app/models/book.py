from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Book:
    db = "book_club"
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.books_favorited = []
        self.users = None

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books(title,description) VALUES(%(title)s,%(description)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books JOIN favorites ON books.id = book_id JOIN users ON users.id = user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_books = []
        for row in results:
            book = cls(row)
            i = {
                "id":row["id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["created_at"],
                "updated_at":row["updated_at"]
            }
            book.users = User(i)
            all_books.append(book)
        return all_books

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM books JOIN users ON users.id = user_id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        row = results[0]
        book = cls(row)
        i = {
            "id":row["id"],
            "first_name":row["first_name"],
            "last_name":row["last_name"],
            "email":row["email"],
            "password":row["password"],
            "created_at":row["created_at"],
            "updated_at":row["updated_at"]
        }
        book.users = User(i)
        return book

    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book["title"]) < 1:
            flash("Title is required.")
            is_valid = False
        if len(book["description"]) < 5:
            flash("Description must be at least 5 characters.")
            is_valid = False
        return is_valid