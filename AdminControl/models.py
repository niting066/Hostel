from django.db import models


class AdminUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True, unique=True)
    password = models.CharField(max_length=30, )
    name = models.CharField(max_length=40, )
