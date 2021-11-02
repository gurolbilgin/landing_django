from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    # It is going to be used once not gonna be updated thus auto_now_add is used instead of auto_now
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
