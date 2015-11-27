import pafy

class Watch(object):
    def __init__(self, url):
        self.url = url


    def get_url(self):
       video = pafy.new(self.url, basic= False)
       best = video.getbest()
       return best.url