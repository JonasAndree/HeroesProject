from django.shortcuts import render

# Create your views here.
#request response cycle

def heroes_home(request):
    context = {
        "title":"Heroes",
    }
    return render(request, "base.html", context)
