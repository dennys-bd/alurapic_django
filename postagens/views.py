from django.shortcuts import render, redirect
from .models import Post, PostForm

def nova(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        profile = request.user.perfis.first()
        Post.objects.create(dono=profile, **form.cleaned_data)
        return redirect('indice')

    return render(request, 'postagens/nova.html', { 'form': form })