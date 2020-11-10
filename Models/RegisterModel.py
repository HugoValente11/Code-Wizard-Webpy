import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        print("Data is", data["username"])
        data["username"] = "username"
        data["fullname"] = "fullname"
        data["password"] = "password"
        data["email"] = "email"

        #Encrypt password
        hashed_pw = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
        print(hashed_pw)

        # Insert object in Database
        id = self.Users.insert({"username": data["username"], "name": data["fullname"], "password": hashed_pw, "email": data["email"]})