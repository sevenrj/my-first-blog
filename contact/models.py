from django.db import models
from django.utils import timezone


class Contact(models.Model):
    societe = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nom 
        return self.societe
