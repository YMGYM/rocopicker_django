from django.shortcuts import render

def mainpage(request):
    
    return render(request, 'picker/mainpage.html')


def inputPage(request):
    
    return render(request, 'picker/inputpage.html')


def resultPage(request):
    
    return render(request, 'picker/resultPage.html')


def creditPage(request):
    
    return render(request, 'picker/creditPage.html')