from django.shortcuts import render
from .models import About

# Create your views here.
# def about(request):

#     return render(request, 'about/about.html')


def about(request):
    about = About.objects.first()  # Récupère la première entrée (s'il y en a une)
    return render(request, 'about/about.html', {'about': about})