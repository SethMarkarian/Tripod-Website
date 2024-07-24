from django.shortcuts import render, get_object_or_404
from .models import Sculpture

def index(request):
    sculptures = Sculpture.objects.all()
    return render(request, 'catalog/index.html', {'sculptures': sculptures})

def about(request):
    return render(request, 'catalog/about.html')

def contact(request):
    return render(request, 'catalog/contact.html')

def sculpture_detail(request, pk):
    sculpture = get_object_or_404(Sculpture, pk=pk)
    return render(request, 'catalog/sculpture_detail.html', {'sculpture': sculpture})
