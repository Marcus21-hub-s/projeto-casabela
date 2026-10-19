from django.shortcuts import render, get_object_or_404
from .models import Movel

def index(request):
    moveis = Movel.objects.all()
    return render(request, 'moveis/index.html', {'moveis': moveis})

def detalhe(request, id):
    movel = get_object_or_404(Movel, id=id)
    return render(request, 'moveis/detalhe.html', {'movel': movel})

# Create your views here.
