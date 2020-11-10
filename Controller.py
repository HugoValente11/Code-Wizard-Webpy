# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:12:36 2020

@author: Hugo
"""
import web
from Models.RegisterModel import RegisterModel
from Models.LoginModel import LoginModel

urls = (
        '/', 'Home',
        '/register', 'Register',
        '/postregistration', 'PostRegistration',
        '/login', 'Login',
        '/check-login', 'CheckLogin'
        )

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()

class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()
        print("Data: ", data)
        data = {"username": "test1", "password": "password1"}
        reg_model = RegisterModel()
        reg_model.insert_user(data)

        return data["username"]

class CheckLogin:
    def POST(self):
        data = web.input()
        print("Check login data:", data)
        login_model = LoginModel()
        isCorrect = login_model.check_login(data)
        if isCorrect:
            return isCorrect
        return "error"


if __name__ == "__main__":
    app.run()