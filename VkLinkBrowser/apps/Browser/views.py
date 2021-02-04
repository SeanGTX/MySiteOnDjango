from django.shortcuts import render
from Browser.models import *
from django.conf import settings

MEDIA_URL = settings.MEDIA_URL

availablePubs = Public.getChildClassesName()

def options(request):
    return render(request, 'Browser/list.html', {'availablePubs': availablePubs, 'MEDIA_URL': MEDIA_URL})

