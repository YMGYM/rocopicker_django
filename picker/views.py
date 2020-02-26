from django.shortcuts import render
# from . import predictapp
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
        score = float(request.POST['score'])
        if score >= 0.7:
            resultMsg = "이건 로코의 퍼스널리티에 저스트-핏! 이네요! 확실해요!"
        elif score >= 0.5:
            resultMsg = "흠.. 조금 로코의 퍼스널리티의 필링이긴 한데..낫-클리어하네요!"
        elif score >= 0.3:
            resultMsg = "이건 로코라고 하기엔 낫-클리어한 인스피레이션이네요..."
        else:
            resultMsg = ".. 이건 로코의 포트레이트는 아니네요!"
            
        result = [score, float(request.POST['score2'])]
        percentage = score * 100
        frame_b64 = request.POST['imageForm']
        
        
        
        return render(request, 'picker/resultPage.html', {'percentage':percentage, 'image':frame_b64, 'resultMsg':resultMsg, 'result':result})
        # ------------------ 서버에서 모델 처리 ---------------------------
        # if 'image' in request.FILES:
        #     try:
        #         model
        #     except NameError:
        #         model = predictapp.load_model()

        #     data = request.FILES['image']
        #     result, frame_b64, percentage, msg = predictapp.predict(model, data)
        # return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage, 'resultMsg':msg})
        # -------------------------------------------------------

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

def errorPage(request):
    return render(request,'picker/error.html')

def error404(request, exception):
    return render(request,'picker/error.html', status=404)

def error500(request):
    return render(request,'picker/error.html', status=500)
