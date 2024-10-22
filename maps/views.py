from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from maps.models import SavedPlace


# Create your views here.
def index(request):
    saved_places = SavedPlace.objects.all()
    return render(request, "index.html", {'saved_places': saved_places})

@csrf_exempt
def save_place(request):
    if request.method == "POST":
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        address = request.POST.get('address')

        SavedPlace.objects.create(address=address, latitude=lat, longitude=lon)
        return JsonResponse({'status': 'success', 'message': 'Location saved successfully!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def get_route(request, location1_id, location2_id):
    try:
        place1 = SavedPlace.objects.get(id=location1_id)
        place2 = SavedPlace.objects.get(id=location2_id)
    except SavedPlace.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'SavedPlace not found'}, status=404)

    coords1 = f"{place1.longitude},{place1.latitude}"
    coords2 = f"{place2.longitude},{place2.latitude}"

    url = f"https://router.project-osrm.org/route/v1/driving/{coords1};{coords2}?overview=full&geometries=geojson"

    response = requests.get(url)
    if response.status_code == 200:
        route_data = response.json()
        return JsonResponse({'status': 'success', 'route': route_data})
    else:
        return JsonResponse({'status': 'error', 'message': 'OSRM API error'}, status=response.status_code)
