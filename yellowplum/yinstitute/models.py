from django.db import models
from yellowplum.models import BaseModel
from yglobal.models import Address

__author__ = 'Hari'



class Institute(BaseModel):
    name = models.CharField(max_length=100),
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True)