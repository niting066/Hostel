from django.db import models


class ContactModel(models.Model):
    first_name = models.CharField(max_length=40, primary_key=True)
    contact = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    query = models.CharField(max_length=200)
