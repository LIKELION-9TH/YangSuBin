from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def hobby(request):
    return render(request, "hobby.html")

def place(request):
    return render(request, "place.html")

def music(request):
    return render(request, "music.html")

def photo(request):
    return render(request, "photo.html")
    
def main(request):
    return render(request, "main.html")