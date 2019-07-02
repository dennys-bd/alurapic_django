from django.db import models
from django import forms
from profiles.models import Profile

class Post(models.Model):
    foto = models.URLField(max_length=511)
    corpo = models.TextField(max_length=4095)
    data_criacao = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(
        Profile,
        models.CASCADE,
        related_name='posts',
        related_query_name='post',
    )

# class PostForm(forms.Form):
#     foto = forms.URLField(max_length=511)
    # corpo = forms.CharField(
    #             max_length=4095, 
    #             widget=forms.Textarea(
    #                 attr={
    #                     'rows': 20,
    #                     'cols': 50,
    #                 }
    #             )
    #         )

class PostForm(forms.ModelForm):
    corpo = forms.CharField(max_length=4095, widget=forms.Textarea(attrs={'placeholder': 'Corpo'}))
    class Meta:
        model = Post
        fields = (
            'foto', 'corpo'
        )

    def clean_corpo(self):
        corpo = self.cleaned_data.get('corpo')
        if 'sonic' in corpo:
            raise forms.ValidationError('No sonic in this field.')
