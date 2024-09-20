from django.shortcuts import render
from .forms import ImageUploadForm
from .models import Image
from .yolo_model import detect_objects  


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            detect_objects(uploaded_image.image.path) 
            return render(request, 'result.html', {'image': uploaded_image})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})
