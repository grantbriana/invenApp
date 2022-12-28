from django.db import models
from django.urls import reverse
import django_tables2 as tables

# Create your models here.

class Member(models.Model):
  id = models.CharField(max_length=255, primary_key=True, unique=True)
  name = models.CharField(max_length=255)
  quantity = models.IntegerField()

  def __str__(self):
      return self.my_field_name

  def get_absolute_url(self):
    """Returns the URL to access a particular instance of the model."""
    return reverse('model-detail-view', args=[str(self.id)])

class Item(models.Model):
    id = models.CharField(max_length=255, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    inventory = models.IntegerField()


    def __str__(self):
        return str(self.inventory) + " " + self.id + " " + self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('item-detail', args=[str(self.id)])