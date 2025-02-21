from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    # Champ pour le nom
    name = models.CharField(max_length=100)

    # Champ pour l'email
    email = models.EmailField()

    # Champ pour le message
    message = models.TextField()

    # Champ pour la date d'envoi
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name}"