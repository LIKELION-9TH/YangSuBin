from django.shortcuts import render, get_object_or_404
from .models import Photo

def home(request):
    return render(request, "home.html")

def hobby(request):
    return render(request, "hobby.html")

def place(request):
    return render(request, "place.html")

def music(request):
    return render(request, "music.html")

def photo(request):
    photos = Photo.objects.all()
    return render(request, "photo.html", {'photos':photos})

def detail(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, "detail.html", {'photo':photo})
    
def main(request):
    return render(request, "main.html")