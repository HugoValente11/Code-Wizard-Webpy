from pymongo import MongoClient


class PostModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Posts = self.db.posts

    def insert_posts(self, data):
        self.Posts.insert({'username': data['username'], 'content': data['content']})

        return True

    def get_all_posts(self):
        posts = self.Posts.find()
        new_posts = []
        for post in posts:
            new_posts.append(post)
        return new_posts

    def get_user_posts(self, user):
        all_posts = self.Posts.find({'username': user})
        new_posts = []
        for post in all_posts:
            new_posts.append(post)
        return new_posts



