from django.shortcuts import render

from .models import Person

# Create your views here.
def index(request):
    return render(request, 'page/home.html')

def dashboard(request):
    context = {
        'profiles': Person.objects.order_by('updated_at').all(),
    }
    return render(request, 'page/dashboard.html', context)

def profile_info(request, id):
    context = {
        'profile': Person.objects.get(id=id)
    }
    return render(request, 'page/profile_info.html', context)
