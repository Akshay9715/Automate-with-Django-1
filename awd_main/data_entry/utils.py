from django.apps import apps

def all_custom_models():
    
    inbuilt_apps = ['LogEntry','Permission','Group','Session','User','ContentType','Uploads']
    custom_models = []
    
    for model in apps.get_models():
        if model.__name__ not in inbuilt_apps:
            custom_models.append(model.__name__)
    return custom_models
    
