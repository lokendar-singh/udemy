from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'relurl_temp/index.html')

def other(request):
    return render(request,'relurl_temp/other.html')

def relurl(request):
    return render(request,'relurl_temp/relurl_temp.html')
