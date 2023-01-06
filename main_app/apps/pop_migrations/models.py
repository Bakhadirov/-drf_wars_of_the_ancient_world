from django.db import models

# Create your models here.

class MainTable(models.Model):
    country = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    population = models.FloatField(null=True)
    pop_density = models.FloatField(null=True)
    net_migration = models.FloatField(null=True)
    migration_perc = models.FloatField(null=True)
    iso3c = models.CharField(max_length=5, null=True)
    iso2c = models.CharField(max_length=5, null=True)
    region = models.CharField(max_length=200, null=True)
    adminregion = models.CharField(max_length=200, null=True)
    incomeLevel = models.CharField(max_length=200, null=True)
    lendingType = models.CharField(max_length=200, null=True)
    capitalCity = models.CharField(max_length=200, null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)