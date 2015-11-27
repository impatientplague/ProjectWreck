import pafy

class Stats(object):
    def __init__(self, url):
        self.url = url

    def get_title(self):
        video = pafy.new(self.url, basic= False)
        title = video.title
        return title

    def get_description(self):
        video = pafy.new(self.url, basic= False)
        desc = video.description
        return desc

    def get_author(self):
        video = pafy.new(self.url, basic= False)
        auth = video.author
        return auth

    def get_views(self):
        video = pafy.new(self.url, basic= False)
        views = video.viewcount
        return format(views,',')

    def get_likes(self):
        video = pafy.new(self.url, basic= False)
        likes = video.likes
        return format(likes,',')

    def get_dislikes(self):
        video = pafy.new(self.url, basic= False)
        dislikes = video.dislikes
        return format(dislikes,',')



#test = Stats('https://www.youtube.com/watch?v=2X_2IdybTV0')
#getit = test.get_description()
#print getit
