from django.shortcuts import render
from django.http import HttpResponse
from core.models import Topic,Webpage,AccessRecord
from core.forms import UserDetialsForm, GenForm
# Create your views here.



def call_form2(request):
    form = GenForm()

    if request.method == 'POST':
        print('** Post function called')
        form = GenForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('** Record Saved')
        else:
            print('** Invalid entry!!')
    #         print('** Name '+ form.cleaned_data['name'])
    #         print('** Email '+ form.cleaned_data['email'])
    #         print('** Text '+ form.cleaned_data['text'])

    return render(request,'core/form.html',{'form_name':form})



def call_form(request):
    form = UserDetialsForm()

    print('** enter in call_form')
    print(str(request.method))
    if request.method == 'POST':
        print('** Post function called')
        form = UserDetialsForm(request.POST)
        if form.is_valid():
            print('** Form is valid')
            print('** Name '+ form.cleaned_data['name'])
            print('** Email '+ form.cleaned_data['email'])
            print('** Text '+ form.cleaned_data['text'])

    return render(request,'core/form.html',{'form_name':form})



def firstpage(request):
    ##########Part 3 to send data to template ###########
    acc_rec = AccessRecord.objects.order_by('date')
    dict_var = {'acc_rec': acc_rec}
    return render(request,'core/temp1.html',context=dict_var)
    ##########Part 2 to send data to template ###########

    # dict_var = {'fname':'Lokendar','lname':'dusra buddha singh'}
    # return render(request,'core/temp1.html',context=dict_var)

    ##########Part 1 to send data to template ###########

    # strHTML = '<b>This is bold text</b>'
    # return HttpResponse('<h1>Our second quick app</h1></br>'+strHTML)
