from django.db import models
from django.db.models.fields import CharField, FloatField

# Create your models here.


class UserModel(models.Model):
    name = CharField(max_length=200)
    age = FloatField(max_length=3)
    email = CharField(max_length=200)
    phone = CharField(max_length=200)
    university = CharField(max_length=200)
    year = CharField(max_length=200)

    def __str__(self):
        return self.name
