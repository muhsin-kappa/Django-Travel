from django.db import models

# Create your models here.

class Meet_the_Team(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='Meet_the_Team')
    description = models.TextField()

    def __str__(self):
        return self.name