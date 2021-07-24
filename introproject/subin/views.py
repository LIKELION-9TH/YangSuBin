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
    new_photo.image = request.FILES['image']
    new_photo.body = request.POST['body']
    new_photo.pub_date = timezone.now()
    new_photo.save()
    return redirect('detail', new_photo.id)

def edit(request, id):
    edit_photo = Photo.objects.get(id=id)
    return render(request, 'edit.html', {'photo':edit_photo})

def update(request, id):
    update_photo = Photo.objects.get(id=id)
    update_photo.title = request.POST['title']
    update_photo.writer = request.POST['writer']
    update_photo.image = request.POST['image']
    update_photo.body = request.FILES['body']
    update_photo.pub_date = timezone.now()
    update_photo.save()
    return redirect('detail', update_photo.id)

def delete(request, id):
    delete_photo = Photo.objects.get(id=id)
    delete_photo.delete()
    return redirect('photo')

def main(request):
    return render(request, "main.html")