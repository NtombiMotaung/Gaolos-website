from django.urls import path
from Gallery.views import gallery


app_name = "gallery"


urlpatterns = [

    path("", gallery, name="get-gallery-page"),
    


]