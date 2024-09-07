from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'data_entry/home.html')


def import_data(request):
    return render(request,'data_entry/import_data.html')
