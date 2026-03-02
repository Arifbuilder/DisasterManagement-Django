from django.urls import path
from .views import nearby_disasters

urlpatterns = [
    path("api/nearby-disasters/", nearby_disasters, name="nearby_disasters"),
]