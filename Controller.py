# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:12:36 2020

@author: Hugo
"""
import web
from Models.RegisterModel import RegisterModel
from Models.LoginModel import LoginModel
from Models.PostModel import PostModel
web.config.debug = False

urls = (
        '/', 'Home',
        '/register', 'Register',
        '/postregistration', 'PostRegistration',
        '/login', 'Login',
        '/check-login', 'CheckLogin',
        '/logout', 'Logout',
        '/post-activity', 'PostActivity',
        '/profile/(.*)/info', 'UserInfo',
        '/settings', 'UserSettings',
        '/profile/(.*)', 'UserProfile',
        '/update-settings', 'UpdateSettings'
        )

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data['user']})


class Home:
    def GET(self):
        data = {'username': 'admin', 'password': 'admin'}

        login_model = LoginModel()
        isCorrect = login_model.check_login(data)
        if isCorrect:
            session_data['user'] = isCorrect

        postsModel = PostModel()
        new_posts = postsModel.get_all_posts()

        return render.Home(new_posts)


class Register:
    def GET(self):
        return render.Register()


class Login:
    def GET(self):
        return render.Login()


class UserSettings:
    def GET(self):
        data = {'username': 'admin', 'password': 'admin'}
        login_model = LoginModel()
        isCorrect = login_model.check_login(data)
        if isCorrect:
            session_data['user'] = isCorrect

        return render.Settings(session_data)


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


class PostActivity:
    def POST(self):
        data = web.input()
        data['username'] = session_data['user']['username']
        print("Data:", data)
        post_model = PostModel()
        post_model.insert_posts(data)
        return "success"


class UpdateSettings:
    def POST(self):
        data = web.input()
        data['username'] = session_data['user']['username']

        settings_model = LoginModel()
        if settings_model.update_info(data):
            return "success"
        return "An error has occured"


class UserInfo:
    def GET(self, user):
        login_model = LoginModel()
        user_info = login_model.get_profile(user)
        return render.Info(user_info)


class UserProfile:
    def GET(self, user):
        login_model = LoginModel()
        user_info = login_model.get_profile(user)

        post_model = PostModel()
        posts = post_model.get_user_posts(user_info)

        print("U info:", user_info)

        return render.Profile(posts, user_info)



if __name__ == "__main__":
    app.run()