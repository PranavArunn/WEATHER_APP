from django.shortcuts import render
from .forms import cityform
from .models import city
import requests

# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=70a23a29d0e8eb860800c9f8de0e6f83"
    if request.method == "POST":
        form = cityform(request.POST)
        form.save()
    
    form = cityform()
    city_name = city.objects.all()
    Weather_data = []
    for i in city_name:
        try :
            r = requests.get(url.format(i)).json()
            city_weather = { "city"   : i.name,
            "temperature" :  r["main"]["temp"],
            "description" :r["weather"][0]["description"],
            "icon" : r["weather"][0]["icon"] }
        except:
            pass
        else:
            Weather_data.append(city_weather)
    
    X = {"Weather_data" : Weather_data, "form" : form}
    return render(request,"Weather/Weather.html",X) 





