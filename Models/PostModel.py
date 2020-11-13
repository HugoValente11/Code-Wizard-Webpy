from pymongo import MongoClient
import datetime
import humanize


class PostModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Posts = self.db.posts
        self.Comments = self.db.comments


    def insert_posts(self, data):
        self.Posts.insert({'username': data['username'], 'content': data['content'], "date_added": datetime.datetime.now()})

        return True

    def get_all_posts(self):
        posts = self.Posts.find().sort('date_added', -1)
        new_posts = []
        for post in posts:
            post['timestamp'] = humanize.naturaltime(datetime.datetime.now() - post['date_added'])

            comments = self.Comments.find({"post_id": str(post['_id'])}).sort('date_added', -1)
            post['comments'] = []
            for comment in comments:
                comment['timestamp'] = humanize.naturaltime(datetime.datetime.now() - comment['date_added'])

                post['comments'].append(comment)
            new_posts.append(post)
        return new_posts

    def get_user_posts(self, user):
        all_posts = self.Posts.find({'username': user}).sort('date_added, -1')
        new_posts = []
        for post in all_posts:
            post['timestamp'] = humanize.naturaldate(datetime.datetime.now() - post['date_added'])
            new_posts.append(post)
        return new_posts

    def add_comment(self, comment):
        inserted = self.Comments.insert({'post_id': comment['post_id'], 'content': comment['comment-text'],
                                         'username': comment['username'], 'date_added': datetime.datetime.now()})
        return inserted




