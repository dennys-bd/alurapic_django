from django.db import models
from profiles.models import Profile

class Post(models.Model):
    foto = models.URLField(max_length=511)
    corpo = models.TextField(max_length=4095)
    data_criacao = models.DateTimeField() # auto_now_add=True
    dono = models.ForeignKey(
        Profile,
        models.CASCADE,
        related_name='posts',
        related_query_name='post',
    )