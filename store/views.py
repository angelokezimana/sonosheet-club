from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Album, Artist, Booking, Contact


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:9]
    return render(request, 'store/index.html', {'albums': albums})


def listing(request):
    albums_list = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 9)
    page = request.GET.get('page')

    try:
        albums = paginator.page(page)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        albums = paginator.page(1)

    return render(request, 'store/listing.html', {'albums': albums, 'paginate': True})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'store/detail.html', {'album': album})


def search(request):
    query = request.GET.get('query')
    title = "Résultats pour la requête %s" % query

    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    return render(request, 'store/search.html', {'albums': albums, 'title': title})
