from django.db import models
from yellowplum.models import BaseModel

__author__ = 'Hari'

class Course(BaseModel):
    name = models.CharField(max_length=50),
    technologies = models.CharField(max_length=150),
    type = models.CharField(max_length=50),
    method = models.CharField(max_length=50),
    description = models.CharField(max_length=500,null=True),
    tutor = models.ForeignKey()

