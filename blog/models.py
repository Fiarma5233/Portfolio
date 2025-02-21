from django.db import models

# Create your models here.
#from django.db import models

class Post(models.Model):
    # Champ pour le titre de l'article
    title = models.CharField(max_length=200)

    # Champ pour le contenu de l'article
    content = models.TextField()

    # Champ pour la date de publication
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title