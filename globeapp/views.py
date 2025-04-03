from django.shortcuts import render
from django.views import View
from .models import Location, SMPost


# Create your views here.
class HomePage(View):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()

        sm_posts = SMPost.objects.all()

        context = {"locations": locations, "sm_posts": sm_posts}
        return render(request, "globeapp/home.html", context=context)
