from django.shortcuts import render
from .models import Render


# Create your views here.
<<<<<<< HEAD
@api_view(["GET", "POST"])
=======
>>>>>>> parent of 9ade060 (changed view to drf)
def index(request):
    obj = Render(name="olakune", description="ola")
    obj.save()
    ans = Render.objects.all().values()
    print(request)

    return render(request, "render/index.html", {"name": list(ans)})
