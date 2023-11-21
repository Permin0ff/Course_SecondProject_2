from django.shortcuts import render
from orm_method.models import Worker


# Create your views here.
def index(request):
    people = Worker.objects.all()
    return render(request, "index.html", {"people": people})
