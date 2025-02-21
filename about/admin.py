from django.contrib import admin

# Register your models here.
from .models import About

# Enregistrer le modèle About dans l'admin
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_image', 'description', 'goals')  # Champs à afficher dans la liste
    search_fields = ('description', 'goals')       # Champs pour la recherche