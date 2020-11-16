from django.shortcuts import render
from django.http import HttpResponse
from .models import Coord
from . import forms

def index(request):
    return HttpResponse("Sei sulla homepage")
    # return render(request,'mappy/index.html')

def coord_form_view (request):
    form = forms.CoordForm()
    if request.method == 'POST':
        form = forms.CoordForm(request.POST)
        if form.is_valid():
            print("Form valido, stampo in console")
            print("indirizzo "+form.cleaned_data['address'])
            print("lat "+str(form.cleaned_data['lat']))
            print("lng "+str(form.cleaned_data['lng']))
            form.save(commit=True)
        else:
            print("error invalid form")

    return render (request, 'mappy/form.html', {'form':form})
