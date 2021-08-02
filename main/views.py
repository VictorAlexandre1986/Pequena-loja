from django.shortcuts import render
from main.models import Item
# Create your views here.
def homepage(request):
    return render(request, template_name='main/home.html')

def itemspage(request):
    items = Item.objects.all()
    return render(request, template_name='main/items.html', context={'items':items})
