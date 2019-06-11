from django.db import models

class List(models.Model):
    text = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return self.text[:50]



