from django.shortcuts import render
from . import predictapp
from PIL import Image
import os
from django.conf import settings

global model
def mainpage(request):
    
    return render(request, 'picker/mainpage.html')


def inputPage(request):
    
    return render(request, 'picker/inputpage.html')


def resultPage(request):
    
    render(request, 'picker/loading.html')
    
    if request.method == "POST":
        try:
            model
        except NameError:
            
            model = predictapp.load_model()
        
        
        data = request.FILES['image']
        result, frame_b64, percentage = predictapp.predict(model, data)
        
    
    return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage})


def sample1predict(request):
    try:
        model
    except NameError:
        
        model = predictapp.load_model()
    
    data = Image.open(os.path.join(settings.STATIC_ROOT,'images/sample1.jpg')).convert('RGB') 
    
    print(data)
    result, frame_b64, percentage = predictapp.predict(model, data)
    
    return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage})
    
def sample2predict(request):
    try:
        model
    except NameError:
        
        model = predictapp.load_model()
    
    data = Image.open(os.path.join(settings.STATIC_ROOT,'images/sample2.jpg')).convert('RGB') 
    
    
    result, frame_b64, percentage = predictapp.predict(model, data)
    
    
    return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage})
def creditPage(request):
    
    return render(request, 'picker/creditPage.html')