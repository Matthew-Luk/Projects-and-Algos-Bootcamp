from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Review:
    db = "flowers"
    def __init__(self,data):
        self.id = data["id"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None

    @classmethod
    def save(cls,data):
        query = "INSERT INTO reviews(description,user_id) VALUES(%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM reviews WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM reviews JOIN users ON user_id = users.id"
        results = connectToMySQL(cls.db).query_db(query)
        all_reviews = []
        for row in results:
            review = cls(row)
            i = {
                "id":row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }
            review.users = User(i)
            all_reviews.append(review)
        return all_reviews

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM reviews WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)