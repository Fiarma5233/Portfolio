from django.db import models

# Create your models here.
#from django.db import models

class About(models.Model):
    # Champ pour une image de profil
    profile_image = models.ImageField(upload_to='about/')

    # Champ pour une description
    description = models.TextField()

    # Champ pour les objectifs
    goals = models.TextField()

    def __str__(self):
        return "À Propos de Moi"