from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO

# Create your views here.

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model('detector/classification_deep_conv_model.h5')


def home(request):
    return render(request, 'index.html')


def predict_image(img):
    img_content = img.read()  # Read the content of the uploaded file
    img = image.load_img(BytesIO(img_content), color_mode='grayscale', target_size=(50, 50))  # Pass the content to load_img
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize to 0-1

    prediction = model.predict(img_array)
    result = np.argmax(prediction, axis=1)

    if result == 0:
        return "mafihch cancer"
    else:
        return "fih cancer"


def result(request):
    if 'img' in request.FILES:
        img_file = request.FILES['img']
        result = predict_image(img_file)
        return render(request, 'result.html', {'result': result})
    else:
        error_message = "No image file uploaded"
        return render(request, 'error.html', {'error_message': error_message})

