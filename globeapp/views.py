from django.shortcuts import render
from django.views import View
from .models import Location


# Create your views here.
class HomePage(View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()

        context = {"locations": locations}
        return render(request, "globeapp/home.html", context=context)
