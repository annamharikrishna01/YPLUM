from yellowplum.models import BaseModel

from django.db import models

class City(BaseModel):
    name = models.CharField(max_length=50),
    state = models.CharField(max_length=100),
    country = models.CharField(max_length=50),
    latitude = models.DecimalField(max_digits=20,decimal_places=10),
    longitude = models.DecimalField(max_digits=20,decimal_places=10)

class Address(BaseModel):
    type = models.CharField(max_length=50),
    hno = models.CharField(max_length=50),
    locality = models.CharField(max_length=50),
    zip = models.IntegerField(max_length=6),
    landmark = models.CharField(max_length=150),
    phone = models.CharField(max_length=50),
    address_line = models.CharField(max_length=150),
    city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True),
    latitude = models.DecimalField(max_digits=20,decimal_places=10),
    longitude = models.DecimalField(max_digits=20,decimal_places=10)

class PersonalInfo(BaseModel):
    about = models.CharField(max_length=500),
    interested = models.CharField(max_length=300),
    achievements = models.CharField(max_length=300)

class ProfessionalInfo(BaseModel):
    about = models.CharField(max_length=500),
    experience = models.CharField(max_length=500),
    achievements = models.CharField(max_length=300),
    interested = models.CharField(max_length=300),
    expertise = models.CharField(max_length=300)









