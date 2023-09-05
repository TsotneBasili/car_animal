from django.urls import path
from Animal import views


urlpatterns = [
    path("", views.SelectAnimalView.as_view(), name="SelectAllAnimals"),
    path("<int:pk>", views.SelectAnimalView.as_view(), name="SelectOneAnimal"),
    path("add", views.AddAnimalVIew.as_view(), name="AddAnimal"),
    path("delete/<int:pk>", views.DeleteAnimalView.as_view(), name="DeleteAnimal")
]
