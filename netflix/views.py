from django.shortcuts import render
from django.conf import settings
import requests
import urllib.request
import urllib
import json
from urllib.parse import quote
from django.contrib.auth.decorators import login_required
# Create your views here.

def movie_now(request):
    if request.method == 'GET':
        category = 'popular'
        movies = []
        # context = {}
        print(settings.MOVIE_DB_API_KEY)
        r = requests.get('https://api.themoviedb.org/3/movie/' + category + '?api_key=' + settings.MOVIE_DB_API_KEY)
        print(r)
        if r.status_code == 200:
            movie = r.json()
            movies.append(movie)
            films = movie['results']
            print(movie['results'])
        # context['favs'] = fav_movie
        return render(request, 'home.html', {'movies':films})
        # json = r.json()
        # serializer = MovieSerializer(data=json)
        # if serializer.is_valid():
        #     movies = serializer.data
        #     return render(request, 'home.html', {'movies':movies})