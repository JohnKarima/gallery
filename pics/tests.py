from django.test import TestCase
from .models import Image, Location, Category
import datetime as dt


class ImageTestClass(TestCase):
    def setUp(self):
        
        self.location = Location(location='bedroom')
        self.location.save_location()

        self.category = Category(category='Real')
        self.category.save_category()

        self.coolpic = Image(id=1, image_name='image', image_description='ya fao really', location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.coolpic, Image))
