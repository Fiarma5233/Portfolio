from django.contrib import admin

# Register your models here.
from .models import ContactMessage

# Enregistrer le modèle ContactMessage dans l'admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent', 'message')  # Champs à afficher dans la liste
    search_fields = ('name', 'email', 'message')   # Champs pour la recherche
    list_filter = ('date_sent',)                   # Filtres pour la liste