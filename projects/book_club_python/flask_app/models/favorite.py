from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    db = "book_club"
    def __init__(self,data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.book_id = data["book_id"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO favorites(user_id,book_id) VALUES(%(user_id)s,%(book_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_users_who_favorited(cls,data):
        query = "SELECT * FROM favorites JOIN users ON users.id = user_id WHERE book_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        all_users = []
        for row in results:
            all_users.append({
                "user_id":row["user_id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"]
                }
            )
        return all_users