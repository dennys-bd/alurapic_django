from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    nome = models.CharField(max_length=63)
    descricao = models.TextField()
    ddn = models.DateField()
    avatar = models.URLField(null=True, blank=True)

    usuario = models.ForeignKey(
        User, 
        models.CASCADE, 
        related_name='perfis', 
        related_query_name='perfil',
    )

    def __str__(self):
        return 'Profile of %s' % self.usuario.username
