from django.db import models
# Create your models here.


class User(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.phone_number