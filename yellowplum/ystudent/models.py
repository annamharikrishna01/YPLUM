from django.db import models
from yellowplum.models import BaseModel
from yglobal.models import Address, PersonalInfo, ProfessionalInfo

__author__ = 'Hari'

class Student(BaseModel):
    first_name = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    display_name = models.CharField(max_length=50),
    mobile = models.CharField(max_length=15),
    email = models.CharField(max_length=50),
    image = models.URLField(max_length=200, null=True),
    gender = models.CharField(max_length=10),
    age = models.IntegerField(max_length=3),
    technologies = models.CharField(max_length=200, null=True),
    cv = models.URLField(max_length=200,null=True),
    res_address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True),
    perm_address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True),
    personal_info = models.ForeignKey(PersonalInfo,on_delete=models.SET_NULL,null=True),
    professional_info = models.ForeignKey(ProfessionalInfo,on_delete=models.SET_NULL,null=True)






