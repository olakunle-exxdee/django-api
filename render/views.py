from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializer


# Create your views here.
@api_view(["GET", "POST"])
def index(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response({"blogs": serializer.data})
