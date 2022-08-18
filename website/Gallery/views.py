from django.shortcuts import render

from Gallery.models import GalleryImages


# Create your views here.
def gallery(request):
    image = GalleryImages.objects.all()
    context = {
        "image" : image,

    }
    
    return render(request, "public/index.html", context)
