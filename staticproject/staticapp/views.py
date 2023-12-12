from django.shortcuts import render
from .models import Place,Team

# Create your views here.
def staticv(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'teams':team})
