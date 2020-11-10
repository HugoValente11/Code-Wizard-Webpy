from pymongo import MongoClient
import bcrypt

class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def check_login(self, data):
        # Find username object
        user_object = self.Users.find_one({"username": data["username"]})

        # Check if user exists
        if user_object:
            # Check if pw matches by comparing hashes
            if bcrypt.checkpw(data["username"].encode(), user_object["password"]):
                print("Code checks out")
                return user_object
            else:
                print("Doesn't check out")
                return False
        else:
            False