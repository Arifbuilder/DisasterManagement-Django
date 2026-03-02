import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .utils import haversine_distance

@login_required
def nearby_disasters(request):
    user = request.user

    if not user.latitude or not user.longitude:
        return JsonResponse({"error": "User location not available"})

    user_lat = float(user.latitude)
    user_lon = float(user.longitude)
    radius_km = request.GET.get("radius", 2000)
    radius_km = float(radius_km)

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "limit": 50,
        "orderby": "time"
    }

    response = requests.get(url, params=params)
    data = response.json()

    nearby = []

    for feature in data["features"]:
        coords = feature["geometry"]["coordinates"]
        disaster_lon = coords[0]
        disaster_lat = coords[1]

        distance = haversine_distance(
            user_lat, user_lon,
            disaster_lat, disaster_lon
        )

        if distance <= radius_km:
            nearby.append({
                "title": feature["properties"]["title"],
                "place": feature["properties"]["place"],
                "magnitude": feature["properties"]["mag"],
                "distance_km": round(distance, 2),
                "latitude": disaster_lat,
                "longitude": disaster_lon
            })

    return JsonResponse({"nearby_disasters": nearby})