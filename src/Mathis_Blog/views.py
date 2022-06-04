from datetime import datetime
from zoneinfo import ZoneInfo

from django.shortcuts import render



def index(request):
    now_in_paris = datetime.now()
    return render(request, "Mathis_Blog/index.html", context={"date": now_in_paris})
