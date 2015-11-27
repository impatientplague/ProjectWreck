import pafy

class Stats(object):
    def __init__(self, url):
        self.url = url

    def get_title(self):
        video = pafy.new(self.url)
        title = video.title
        return title

    def get_description(self):
        video = pafy.new(self.url)
        desc = video.description
        return desc

    def get_author(self):
        video = pafy.new(self.url)
        auth = video.author
        return auth

    def get_views(self):
        video = pafy.new(self.url)
        views = video.viewcount
        return views

    def get_likes(self):
        video = pafy.new(self.url)
        likes = video.likes
        return likes

    def get_dislikes(self):
        video = pafy.new(self.url)
        dislikes = video.dislikes
        return dislikes



#test = Stats('https://www.youtube.com/watch?v=2X_2IdybTV0')
#getit = test.get_description()
#print getit
