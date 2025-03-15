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



'''
{% extends 'base.html' %}
{% load static %}

{% block content %}
<link rel="stylesheet" href="{% static 'skill/css/skill.css' %}">
<div class="skills-container">
    <h2>Mes Expériences et Certifications</h2>

    <!-- Grille des expériences (2x2) -->
    <div class="skills-grid">
        {% for experience in page_obj %}
        <div class="experience-card">
            <h3>{{ experience.title }}</h3>
            <p class="organization">{{ experience.organization }} - {{ experience.year }}</p>
            <p class="description">{{ experience.description }}</p>
            {% if experience.certification_file %}
            <a href="{{ experience.certification_file.url }}" target="_blank" class="certification-link" download>Voir la certification</a>
            {% endif %}
        </div>
        {% endfor %}
    </div>

    <!-- Pagination -->
    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1" class="pagination-link">&laquo; Première</a>
                <a href="?page={{ page_obj.previous_page_number }}" class="pagination-link">Précédente</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} sur {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}" class="pagination-link">Suivante</a>
                <a href="?page={{ page_obj.paginator.num_pages }}" class="pagination-link">Dernière &raquo;</a>
            {% endif %}
        </span>
    </div>
</div>
{% endblock %}
'''

