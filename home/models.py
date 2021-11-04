from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.related import ForeignKey

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


class Branch(models.Model):
    branch = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.branch


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_teacher = models.EmailField(max_length=254)
    phone_teacher = models.CharField(max_length=50)
    image = models.ImageField(upload_to="teacher", default='default.png')
    created_date = models.DateTimeField(auto_now_add=True)
    speciality = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
