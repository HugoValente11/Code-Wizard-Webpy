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
            if bcrypt.checkpw(data["password"].encode(), user_object["password"]):
                print("Code checks out")
                return user_object
            else:
                print("Doesn't check out")
                return False
        else:
            False

    def update_info(self, data):
        self.Users.update_one({'username': data['username']}, {"$set": data})
        return True

    def get_profile(self, user):
        user_info = self.Users.find_one({'username': user})
        return user_info
