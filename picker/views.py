from django.shortcuts import render
from . import predictapp
from PIL import Image
import os
from django.conf import settings
import numpy as np
global model

def mainpage(request):
    
    return render(request, 'picker/mainpage.html')


def inputPage(request):
    
    return render(request, 'picker/inputpage.html')


def resultPage(request):

    
        
    
    if request.method == "POST":  
        if 'image' in request.FILES:
            try:
                model
            except NameError:
                model = predictapp.load_model()

            data = request.FILES['image']
            result, frame_b64, percentage, msg = predictapp.predict(model, data)


            return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage, 'resultMsg':msg})

    return render(request, 'picker/error.html')
def sample1predict(request):
    try:
        model
    except NameError:
        
        model = predictapp.load_model()
    
    data = Image.open(os.path.join(settings.STATICFILES_DIRS[0],'images/sample1.jpg')).convert('RGB') 
    
    result, frame_b64, percentage, msg = predictapp.predict(model, data)
    
    
    
    return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage, 'resultMsg':msg})
    
    
def sample2predict(request):
    try:
        model
    except NameError:
        
        model = predictapp.load_model()
    
    data = Image.open(os.path.join(settings.STATICFILES_DIRS[0],'images/sample2.jpg')).convert('RGB') 
    
    
    result, frame_b64, percentage, msg = predictapp.predict(model, data)
    
    
    return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage, 'resultMsg':msg})


def creditPage(request):
    
    return render(request, 'picker/creditPage.html')


def error404(request, exception):
    return render(request,'picker/error.html', status=404)

def error500(request):
    return render(request,'picker/error.html', status=500)


def tftest(request):
    return render(request, 'picker/tftest.html')