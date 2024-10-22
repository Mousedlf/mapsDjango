from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save-location/", views.save_place, name="save_location"),
    path('get-route/<int:location1_id>/<int:location2_id>/', views.get_route, name='get_route'),

]