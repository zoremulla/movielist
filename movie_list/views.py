from django.shortcuts import render
import requests
# Create your views here.
def movies_list(request):
    query=request.GET.get("q")
    url="http://www.omdbapi.com/?apikey=845c2d09&s=Lord"
    if query:
        url="http://www.omdbapi.com/?apikey=845c2d09&s=" + query
    response=requests.get(url)
    print(response.json())
    context={
        'movies': response.json()
    }

    return render(request, 'list.html', context)

def movies_detail(request, movie_id):
    url="http://www.omdbapi.com/?apikey=845c2d09&i=" + movie_id
    response=requests.get(url)
    context={
        'movie':response.json()
    }
    return render(request,'detail.html', context)