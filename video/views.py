from django.shortcuts import render

from .models import Video
# Create your views here.

def index(request):
    """[summary]

    Args:
        request ([type]): [description]
    """
    videos = Video.objects.all()
    return render(request, "index.html", {'videos': videos})
