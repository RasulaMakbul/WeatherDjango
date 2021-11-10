from django.shortcuts import render



def home(request):
    import json
    import requests

    api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20022&distance=25&API_KEY=036897F4-2EF1-4134-B621-48E47C9DC954")
    
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api ="Error..."

    if api.0.Category.Name == "Good":
        category_description="(0-50)Air quality is considered satisfactory, and air pollution poses little or no risk."

    elif api.0.Category.Name == "Moderate":
        category_description="(51-100)"
    elif api.0.Category.Name == "USG":
        category_description="(101-150)"
    elif api.0.Category.Name == "Unhealty":
        category_description="(151-200)"
    elif api.0.Category.Name == "Very Unhealty":
        category_description="(201-250)"
    elif api.0.Category.Name == "Hazardous":
        category_description="(251 or above)"
    
    return render(request, 'home.html' , {'api': api})
def about(request):
    return render(request, 'about.html' , {})
