from django.shortcuts import render
from .models import Render


# Create your views here.


def index(request):
    obj = Render(name="olakune", description="ola")
    obj.save()
    ans = Render.objects.all().values()
    print(request)

    return render(request, "render/index.html", {"name": list(ans)})
