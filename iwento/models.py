from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Country_1 = 'Brasil'
    Country_2 = 'Argentina'
    destiny = models.CharField(max_length=1, choices=
    ((Country_1,'Peru'),
    (Country_2,'Chile'),
    ))
