from django.shortcuts import render
from .models import equipment

# Create your views here.

def equipamiento (request):
    equipmento = equipment.objects.all()
    return render(request,"index.html", {"equipmento": equipmento})