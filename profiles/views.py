from django.shortcuts import render
# from django.http import HttpResponse

# def indice(request):
#     return HttpResponse('Olarrr Mundo!')

# def detalhe(request, id):
#     return HttpResponse('Nosso Detalhe! Perfil %d' % id)

def indice(request):
    return render(request, 'profiles/indice.html', {})

def meu_perfil(request):
    return render(request, 'profiles/detalhe.html', {'perfil_id': request.user.id})

def detalhe(request, id):
    return render(request, 'profiles/detalhe.html', {'perfil_id': id})
