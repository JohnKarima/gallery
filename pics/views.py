from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category

# Create your views here.
def welcome(request):
    '''
    Method to return our images, locations & categories
    '''
    images = Image.objects.all()
    location = Location.objects.all()
    categories = Category.get_all_categories()
    context = {
        "images":images,
        "location":location,
        "categories": categories,
    }

    return render(request, 'welcome.html' , context)