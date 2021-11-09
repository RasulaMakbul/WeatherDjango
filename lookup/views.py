from django.shortcuts import render



def home(request):
    import json
    import requests

    api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=036897F4-2EF1-4134-B621-48E47C9DC954")
    
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api ="Error..."

    
    return render(request, 'home.html' , {'api': api})
def about(request):
    return render(request, 'about.html' , {})
