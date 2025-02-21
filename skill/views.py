from django.shortcuts import render
from .models import  Experience

# Create your views here.

def skill(request):
    experiences = Experience.objects.all()

    return render(request, 'skill/skill.html', {'experiences': experiences})