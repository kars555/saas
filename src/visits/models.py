from django.db import models

# Create your models here.

# building a database using django model which inheritance from models.Model


class PageVisit(models.Model):
    # specific it is a column that store text
    path = models.TextField(blank=True, null=True)
    # specific it is column for data and time
    timestamp = models.DateTimeField(auto_now_add=True)
