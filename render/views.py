from django.shortcuts import render
from .models import Render


# Create your views here.
def index(request):
    obj = Render(name="olakune", description="ola")
    obj.save()
    ans = Render.objects.all().values()
    print(request)
<<<<<<< HEAD
    return render(request, "render/index.html", {"name": list(ans)})
=======
    return render(
        request,
        "render/index.html",
    )
>>>>>>> parent of 118b6b8 (let goo)
