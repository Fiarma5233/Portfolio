from django.shortcuts import render
from .models import  Experience

# Create your views here.

def skill(request):
    experiences = Experience.objects.all().order_by('-year')  # Trier par année décroissante

    return render(request, 'skill/skill.html', {'experiences': experiences})