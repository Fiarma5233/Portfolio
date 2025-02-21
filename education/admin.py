from django.contrib import admin

# Register your models here.
from .models import Education

# Enregistrer le modèle Education dans l'admin
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year')  # Champs à afficher dans la liste
    search_fields = ('degree', 'institution')        # Champs pour la recherche
    list_filter = ('end_year',)                         # Filtres pour la liste