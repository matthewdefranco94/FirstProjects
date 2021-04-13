import datetime

from django.utils import timezone
from django.db import models


# Create your models here.
# models.model = inheritance, used when when you want a new class to behave like a previous / similar class
# models generally map to a database
# running 'makemigrations' allows your Django to know that you're made changes to your models
# migrations are how Django stores changes in our models and thus, our database schema
# sqlmigrate command takes migration names and returns their SQL

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date_Published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)


class Choice(models.Model):
    #each CHOICE is related to a simple QUESTION
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self): #when you try to call this object, it will be 'converted' to a string
        return self.choice_text

# change your models (in models.py)
# Run 'python manage.py makemigrations' to create migrations for those changes
# Run 'python manage.py migrate' to apply those changes to the database