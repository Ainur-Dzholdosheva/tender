from django.db import models


class Tender(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=255)


    def __str__(self):
        return self.name