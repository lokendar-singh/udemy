from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'temp_app_folder/index.html')

def other(request):
    return render(request,'temp_app_folder/other.html')

def relative_view(request):
    return render(request,'temp_app_folder/relative.html')
