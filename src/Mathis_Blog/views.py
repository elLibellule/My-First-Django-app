from datetime import datetime
from zoneinfo import ZoneInfo

from django.shortcuts import render

def index(request):
    return render(request, "Mathis_Blog/index.html", context={"date": datetime.now(tz=ZoneInfo("Europe/Paris"))})
