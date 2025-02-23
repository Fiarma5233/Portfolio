from django.db import models

# Create your models here.
# realisations/models.py
# from django.db import models

class Realisation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la réalisation")
    link = models.URLField(verbose_name="Lien vers la réalisation")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Réalisation"
        verbose_name_plural = "Réalisations"