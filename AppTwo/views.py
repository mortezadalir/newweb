from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms
# Create your views here.
def index(request):
    form=forms.FormName()
    if request.method == 'POST':
        form= forms.FormName(request.POST)
        if form.is_valid():
            #User.FirstName=form.cleaned_data['FirstName']
           # LastName=form.cleaned_data['LastName']
          #  Email=form.cleaned_data['Email']
            users = User.objects.get_or_create(FirstName=form.cleaned_data['FirstName'],
                                          LastName=form.cleaned_data['LastName'],
                                          Email=form.cleaned_data['Email'],
                                          text=form.cleaned_data['text'])
            print(form.cleaned_data['FirstName'])
    return render(request,'AppTwo/index.html',{'form':form})
    
    
def users(request):
    my_user=User.objects.order_by()
    my_dict1={'my_content1': my_user}
    return render(request,'AppTwo/users.html',context=my_dict1)