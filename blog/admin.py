from django.contrib import admin

# Register your models here.
from .models import Post

# Enregistrer le modèle Post dans l'admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted')  # Champs à afficher dans la liste
    search_fields = ('title', 'content')     # Champs pour la recherche
    list_filter = ('date_posted',)           # Filtres pour la liste