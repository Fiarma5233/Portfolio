# from django.contrib import admin

# # Register your models here.
# from .models import Experience

# # Enregistrer le modèle Experience dans l'admin
# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ('title', 'organization', 'year')  # Champs à afficher dans la liste
#     search_fields = ('title', 'organization')        # Champs pour la recherche
#     list_filter = ('year',)                          # Filtres pour la liste

from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'year', 'certification_file')
    search_fields = ('title', 'organization')
    list_filter = ('year',)