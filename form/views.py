from django.shortcuts import render
from . import forms

def index(req) :
    return render(req, 'index.html')

def formAPI(req) :
    if req.method == 'POST' :
        form = forms.DjangoForm(req.POST, req.FILES)
        if form.is_valid() :
            print(form.cleaned_data)
            # return render(req, 'form.html', {'form' : form})
    form = forms.DjangoForm()
    return render(req, 'form.html', {'form' : form})
