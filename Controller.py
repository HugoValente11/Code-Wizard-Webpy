# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:12:36 2020

@author: Hugo
"""
import web
from Models.RegisterModel import RegisterModel
from Models.LoginModel import LoginModel
web.config.debug = False

urls = (
        '/', 'Home',
        '/register', 'Register',
        '/postregistration', 'PostRegistration',
        '/login', 'Login',
        '/check-login', 'CheckLogin',
        '/logout', 'Logout'
        )

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data['user']})



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
            session_data['user'] = isCorrect
            return isCorrect

        return "error"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"


if __name__ == "__main__":
    app.run()