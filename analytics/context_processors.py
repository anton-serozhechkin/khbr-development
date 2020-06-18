from .models import Links, Category

def links(request):
    links = Links.objects.all()
    return {'links': links}

def categories_header(request):
    categories = Category.objects.all()
    return {'categories': categories}