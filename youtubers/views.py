from django.shortcuts import render,get_object_or_404
from .models import Youtuber
# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    if request.method == 'POST':
        if 'city' in request.POST:
            city = request.POST['city']
            if city:
                tubers = tubers.filter(city__iexact = city)
    
        if 'camera_type' in request.POST:
            camera_type = request.POST['camera_type']
            if camera_type:
                tubers = tubers.filter(camera_type__iexact = camera_type)
    
        if 'category' in request.POST:
            category = request.POST['category']
            if category:
                tubers = tubers.filter(category__iexact = category)

    data = {
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search

    }
    return render(request,'youtubers/youtubers.html',data)

def youtuber_details(request,id):
    # tuber = Youtuber.objects.filter(id = id)
    tuber = get_object_or_404(Youtuber,pk = id)
    data = {
        'yt' : tuber,
        'tuberid' : id,
    }
    return render(request,'youtubers/individual_page.html',data)

def youtuber_search(request):
    tubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(desc__icontains = keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact = city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact = camera_type)
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact = category)
    
    data = {
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search

    }
    return render(request,'youtubers/search.html',data)
