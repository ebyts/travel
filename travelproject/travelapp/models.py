from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField(max_length=100)

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='pics')
    description1=models.TextField(max_length=100)

    def __str__(self):
        return self.name1
