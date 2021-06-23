from django.urls import path
from .views import CarListCreateView, CarRetriveUpdeteDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarRetriveUpdeteDeleteView.as_view(), name='car_retrive_update_delete')
]
