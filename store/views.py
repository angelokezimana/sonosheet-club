# from django.shortcuts import render
from django.http import HttpResponse

# from .models import ALBUMS


def index(request):
    message = "Learning Django"
    return HttpResponse(message)


def listing(request):
    albums = [f"<li>{ album['name'] }" for album in ALBUMS]
    message = f"<ul>{ ''.join(albums) }</ul>"
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = f"Le nom de l'album est { album['name'] }. Il a été écrit par { artists }"
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')

    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join([artist['name'] for artist in album['artists']])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = [f"<li>{ album['name'] }</li>" for album in albums]
            message = f"""
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    { "".join(albums) }
                </ul>
            """

    return HttpResponse(message)
