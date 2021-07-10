from django.db import models
from django.utils import timezone


class Genre(models.Model):
    G_name = models.CharField(max_length=30,null=False, blank=False)

    def __str__(self):
        return self.G_name


class Language(models.Model):
    L_name = models.CharField(max_length=30,null=False, blank=False)

    def __str__(self):
        return self.L_name


class Book(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    Author = models.CharField(max_length=100, null=False, blank=False)
    Genres = models.ManyToManyField(Genre,related_name='gbooks')
    Languages = models.ManyToManyField(Language,related_name='lbooks')
    added_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Name 


