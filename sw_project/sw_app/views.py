from django.shortcuts import render
from . models import resources

# Create your views here.


def goto_index(request):
    sampl_img = resources.objects.all()
    return render(request, 'index.html', {'obj': sampl_img})
