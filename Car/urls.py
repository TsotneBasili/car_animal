from django.urls import path
from Car import views


urlpatterns = [
    path("", views.SelectCarView.as_view(), name="SelectAllCars"),
    path("<int:pk>", views.SelectCarView.as_view(), name="SelectOneCars"),
    path("add", views.AddCarVIew.as_view(), name="AddCar"),
    path("delete/<int:pk>", views.DeleteCarView.as_view(), name="DeleteCar")
]
