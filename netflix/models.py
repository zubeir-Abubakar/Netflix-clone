from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.

class Playlist(models.Model):
    movie_title = models.CharField(max_length =420)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.movie_title
    
    def save_playlist(self):
        self.save()
        
class Movie(object):
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
    