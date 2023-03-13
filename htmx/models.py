from django.db import models
from django.db.models.functions import Lower

# Create your models here.
class Film(models.Model):
  name=models.CharField(max_length=128, unique=True)
  order = models.PositiveSmallIntegerField()
  photo = models.ImageField(upload_to="film_photos/", null=True, blank=True)
  
  class Meta:
    ordering = ["order"]
    # ordering = [Lower("")]


class Course(models.Model):
  name = models.CharField(max_length=124)


class Modules(models.Model):
  name = models.CharField(max_length=124)
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")


class GDP(models.Model):
  name = models.CharField(max_length=100)
  capital = models.CharField(max_length=100)
  population = models.PositiveSmallIntegerField()
  currency = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name


class Languages(models.Model):
  name = models.CharField(max_length=100)
  country = models.ForeignKey(GDP, on_delete=models.CASCADE, related_name="languages")