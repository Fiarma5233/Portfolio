# from django.db import models

# # Create your models here.

# class Experience(models.Model):
#     # Champ pour le titre de l'expérience
#     title = models.CharField(max_length=200)

#     # Champ pour l'organisation
#     organization = models.CharField(max_length=200)

#     # Champ pour l'année
#     year = models.CharField(max_length=50)

#     # Champ pour la description
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.title} - {self.organization}"


from django.db import models
from cloudinary.models import CloudinaryField  # Importer CloudinaryField


class Experience(models.Model):
    title = models.CharField(max_length=200)  # Titre de la certification
    organization = models.CharField(max_length=200)  # Organisation émettrice
    year = models.CharField(max_length=50)  # Année d'obtention
    description = models.TextField()  # Description de la certification
    # certification_file = models.FileField(upload_to='certifications/', blank=True, null=True)  # Fichier de certification
    #certification_file = CloudinaryField('certifications', resource_type='auto', blank=True, null=True)
    certification_file = CloudinaryField('certifications', resource_type='raw', format="pdf", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.organization}"