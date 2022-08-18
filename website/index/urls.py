from django.urls import path
from Gallery.views import gallery


app_name = "index"


urlpatterns = [

    path("", gallery, name="get-index-page"),
    


]