from django.shortcuts import render
from .models import Render


# Create your views here.
def index(request):
    obj = Render(name="olakunle", description="lorem")
    obj.save()
    ans = Render.objects.all().values()
    print(request)
    return render(request, "render/index.html", {"product": ans})
