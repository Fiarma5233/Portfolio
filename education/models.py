from django.db import models

# Create your models here.


class Education(models.Model):
    # Champ pour le diplôme
    degree = models.CharField(max_length=200)

    # Champ pour l'établissement
    institution = models.CharField(max_length=200)

    # Champ pour l'année
    start_year = models.CharField(max_length=50)

    #annee d'obtention du diplome
    end_year = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.degree} - {self.institution}"