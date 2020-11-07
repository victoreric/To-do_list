from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, default='')
    priority = models.CharField(max_length=50, default='')
    subitem = models.TextField(max_length=300, default='', blank=True)


    def __str__(self):
        return self.item + ', ' + str(self.completed)