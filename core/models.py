from django.db import models


class Tender(models.Model):
    price=models.CharField(max_length=255, null=True, blank=True)
    number=models.CharField(max_length=255, null=True, blank=True)
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=255)
    buyer=models.CharField(max_length=255, null=True, blank=True)
    participant=models.CharField(max_length=255, null=True, blank=True)
    


    def __str__(self):
        return self.name

class Buyer(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.name

class RedFlag(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.name