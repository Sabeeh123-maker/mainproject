from shop.models import Category

def links(request):
    categories = Category.objects.all()
    return {'cat': categories}