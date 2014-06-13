from django.db import models

# Create your models here.
class Poll(models.Model):
 question = models.CharField(max_length=600)

class Choice(models.Model):
 poll = models.ForeignKey(Poll)
 choice_text = models.CharField(max_length=600)

class Category(models.Model): 
 choice = models.ForeignKey(Choice)
 category = models.CharField(max_length=100)
 weight = models.IntegerField()

class Results(models.Model): 
 user = models.IntegerField()
 poll = models.IntegerField()
 choice = models.IntegerField() 
