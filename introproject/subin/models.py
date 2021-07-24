# from introproject.subin.views import update
from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True, null = True)
    # image = models.ImageField(default)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]