from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Experience

def skill(request):
    # Récupérer toutes les expériences triées par année décroissante
    experiences = Experience.objects.all().order_by('-year')

    # Pagination : 4 expériences par page
    paginator = Paginator(experiences, 4)
    page_number = request.GET.get('page')  # Récupérer le numéro de page depuis l'URL
    page_obj = paginator.get_page(page_number)  # Obtenir les objets de la page actuelle

    return render(request, 'skill/skill.html', {'page_obj': page_obj})