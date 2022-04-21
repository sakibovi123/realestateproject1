from django.http import Http404
from django.shortcuts import render
from django.views import View
from .models import Area
from django.http import Http404
import requests
import json

class HomeView(View):
    template_name = "home/index.html"
    def get(self, request):
        query = Area.objects.all()
        args = {
            "query": query,
            
        }
        return render(request, self.template_name, args)



def search_location(request):
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
    location = request.POST['location']
    querystring = {
        "location":location,
        "home_type":"Houses",
        
        }

    headers = {
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com",
        "X-RapidAPI-Key": "4fe93e20ffmsh157f5635f5f176cp1d6698jsn8e0c7cc18cc6"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = json.loads(response.text)
    print(data)
    args = {"data": data}
    return render(request, "home/search.html", args)

