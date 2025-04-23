from django.db import models


# OopCompanion:suppressRename

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ward(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
