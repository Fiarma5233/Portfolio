from django.shortcuts import render

# Create your views here.
# realisations/views.py
# from django.shortcuts import render
from .models import Realisation

def realisation(request):
    realisations = Realisation.objects.all().order_by('-created_at')
    return render(request, 'footer.html', {'realisations': realisations})