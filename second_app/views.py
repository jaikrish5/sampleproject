from django.shortcuts import render
from . import forms
from second_app.forms import FormNameForm


# Create your views here.

def index(request):

    return render(request,'second_app/index.html')


def form_name_view(request):
    form = forms.FormNameForm()

    if request.method =='POST':

        form = forms.FormNameForm(request.POST)

        if form.is_valid():

                form.save(commit=True)
                return index(request)

        else:
            print('error please check')


    return render(request,'second_app/form_page.html',{'form':form})
