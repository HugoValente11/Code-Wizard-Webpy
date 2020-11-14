import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        #Encrypt password
        hashed_pw = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())

        # Insert object in Database
        id = self.Users.insert({"username": data["username"], "name": data["fullname"],
                                "password": hashed_pw, "email": data["email"], 'avatar': ' ',
                                'background': ' ', 'about': ' ', 'hobbies': ' ', 'birthday': ' '})
        print(id)
        print(data["username"], data["fullname"], hashed_pw, data["email"])
