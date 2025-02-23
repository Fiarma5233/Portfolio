from django.contrib import admin

# Register your models here.
# realisations/admin.py
# from django.contrib import admin
from .models import Realisation

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)