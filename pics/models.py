from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)    
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        '''
        class method to display images by date posted
        '''
        ordering = ['pub_date']

    def __str__(self):
        return self.image_description


class Location(models.Model):
    location = models.CharField(max_length =30)


class Category(models.Model):
    category = models.CharField(max_length =30)

