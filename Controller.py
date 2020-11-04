# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:12:36 2020

@author: Hugo
"""
import web

urls = (
        '/', 'Home'
        )

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())


class Home:
    def GET(self):
        return render.Home()



if __name__ == "__main__":
    app.run()