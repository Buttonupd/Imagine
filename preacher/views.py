from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Location, Image, categories

def home(request):
    category = categories.objects.all()
    images = Image.objects.all()
    location = Location.objects.all()

    if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)

    elif 'category' in request.GET and request.GET['category']:
        cat = request.GET.get('categories')
        images = Image.view_category(cat)
        return render(request, 'all-images.html', {'name':name, 'images':images, 'cat':cat})
    return render(request, 'all-images.html', {'images': images, 'category':category, 'location': location} )

