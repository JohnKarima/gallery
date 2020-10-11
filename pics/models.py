from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)    
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    gallery_image = models.ImageField(upload_to = 'gallery/', null=True)

    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ['pub_date']

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(category__category__icontains=search_term)
        return pics

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def delete_image(self):
        '''
        Method to delete our images
        '''
        self.delete()

    def save_image(self):
        '''
        Method to save our images
        '''
        self.save()

   

   
    def __str__(self):
        return self.image_description


class Location(models.Model):
    location = models.CharField(max_length =30)


    @classmethod
    def get_all_locations(cls):
        '''
        Method to get all the locations
        '''
        locations = cls.objects.all()
        return locations

    def save_location(self):
        '''
        Method to save locations
        '''
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

    
    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length =30)

    @classmethod
    def get_all_categories(cls):
        '''
        Method to get all our categories
        '''
        categories = cls.objects.all()
        return categories

    def save_category(self):
        '''
        Method to save our categories
        '''
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()


    def __str__(self):
        return self.category
