import factory
from postagens.models import Post

class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post

    foto = factory.Faker('image_url')
    corpo = factory.Faker('paragraph')
    data_criacao = factory.Faker('date_this_month')