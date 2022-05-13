from django.db import models

# Create your models here.


class Task(models.Model):  # Task is the name of the table in the database, this basically creates two columns the name and the date
    """Creating the task table in my database"""
    name = models.CharField(max_length=500)
    # auto_now_add will help you to create the time which an item was create
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''This will help to return the actual name of the task assigned instead of the default value'''
        return self.name

    # this line will help us to order our items in descending order, because of the negative parameter passed
    class Meta:
        ordering = ['-id']
