from django.test import TestCase
from .models import Editor,Image,tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):

    def setUp(self):
        self.james= Editor(first_name = 'James', last_name = 'Muriuki', email = 'james"moringaschool.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

class ImageTestClass(TestCase):
    
    def setUp(self):
        # Creating a new image and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',editor = self.james)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()