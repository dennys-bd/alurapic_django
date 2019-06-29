from django.shortcuts import render
from postagens.models import Post
# from django.http import HttpResponse

# def indice(request):
#     return HttpResponse('Olarrr Mundo!')

# def detalhe(request, id):
#     return HttpResponse('Nosso Detalhe! Perfil %d' % id)

def indice(request):
    posts = Post.objects.all().order_by('-data_criacao')

    return render(request, 'profiles/timeline.html', {'posts': posts})

def meu_perfil(request):
    return render(request, 'profiles/timeline.html', {'perfil_id': request.user.id})

def detalhe(request, id):
    return render(request, 'profiles/detalhe.html', {'perfil_id': id})
