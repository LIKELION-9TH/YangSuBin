from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def photo(request):
    return render(request, "photo.html")