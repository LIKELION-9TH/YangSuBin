from django.shortcuts import redirect, render, get_object_or_404
from .models import Photo
from django.utils import timezone

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

def new(request):
    return render(request, "new.html")

def create(request):
    new_photo = Photo()
    new_photo.title = request.POST['title']
    new_photo.writer = request.POST['writer']
    new_photo.body = request.POST['body']
    new_photo.pub_date = timezone.now()
    new_photo.save()
    return redirect('detail', new_photo.id)

def main(request):
    return render(request, "main.html")