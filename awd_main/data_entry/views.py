from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from .utils import *
from data_entry.models import Uploads
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'data_entry/home.html')


def import_data(request):
    all_models = all_custom_models()
    context = {
            'all_models' : all_models,
    }
    if request.method == 'POST':
       file_path = request.FILES.get('file_path')
       model_name = request.POST.get('model_name')
       
       upload = Uploads.objects.create(file=file_path,model_name=model_name)
       relative_path = str(upload.file.url)
       base_path = str(settings.BASE_DIR)

       file_path = base_path + relative_path
    #    file_path = upload.file.name  # This gives you the relative file path in the storage
    
    # # Get the absolute path using default_storage
    #    file_path = default_storage.path(file_path)
       print(file_path)
       try:   
           call_command('insertdataCSV',file_path,model_name)
           messages.success(request,"Your Data Inserted SUCCESSFULLY....")
       except Exception as e:
           messages.error(request,e)

       return redirect('import_data')

    else:
        all_models = all_custom_models()
        context = {
            'all_models' : all_models,
        }
        return render(request,'data_entry/import_data.html',context)
