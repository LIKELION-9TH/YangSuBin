from django.contrib import admin
from django.urls import path
from subin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('hobby/', views.hobby, name="hobby"),
    path('place/', views.place, name="place"),
    path('music/', views.music, name="music"),
    path('photo/', views.photo, name="photo"),
    path('<str:id>', views.detail, name="detail"),
    path('main/', views.main, name="main"),
]
