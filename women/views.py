from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
def index(request): # HttpRequest
    return HttpResponse("Сторінка women")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Сторінка категорій</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Сторінка категорій</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=['music'])
        return redirect(uri)
    
    return HttpResponse(f"<h1>Аріхв по рокам</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Стоірнку не знайшли</h1>")
    # return render(request, '404.html', status=404)