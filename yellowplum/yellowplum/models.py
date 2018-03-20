from datetime import datetime
from django.db import models

__author__ = 'Hari'

class BaseModel(models.model):
    id = models.AutoField(primary_key=True),
    created_at = models.DateTimeField(default=datetime.now())
    modified_t = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or not self.create_at:
            self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()
        super(BaseModel, self).save(*args, **kwargs)

    def delete(self):
        self.is_active = False
        super(BaseModel, self).save()

    def hardDelete(self):
        super(BaseModel, self).delete(self)