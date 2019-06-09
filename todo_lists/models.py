from django.db import models

class List(models.Model):
    text = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return self.text[:50]

class User(models.Model):
    username = models.CharField(max_length = 50)
    name     = models.CharField(max_length = 50)
    passwd   = models.CharField(max_length = 50)
    email    = models.EmailField()

    def __str__(self):
        return self.name


