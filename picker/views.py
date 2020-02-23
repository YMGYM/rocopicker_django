from django.shortcuts import render

def mainpage(request):
    
    return render(request, 'picker/mainpage.html')