from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request response cycle
def heroes_home(request):
    context = {
        "title":"Heroes",
    }
    return render(request, "index.html", context)