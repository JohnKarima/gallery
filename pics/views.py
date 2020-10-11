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

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_description(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})