from django.http.response import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name','Hyderabad')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=b803cfd77873c48f887c11f0f1d5c83f'

        data = requests.get(url).json()

        if data['cod'] == 200:

            print(data['cod'])

            weather_data = {

                'city': city_name,
                'weather': data['weather'][0]['main'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'country': data['sys']['country'],
                'temperature': int(data['main']['temp_max']-273),
                
                }


            context = {
                'weather_data': weather_data,
            }
            return render(request, 'home.html', context)
        else:
            return HttpResponse('City Does Not Exist')

    return render(request, 'home.html')
