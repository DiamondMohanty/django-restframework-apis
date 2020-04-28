from django.db import models

# Create your models here.


class TODO(models.Model):

    description = models.CharField(max_length=255, blank=False, null=False)
    completion_date = models.DateTimeField()
    status = models.BooleanField(default=False)
