from django.core.management.base import BaseCommand
from django.apps import apps
import datetime
import csv


class Command(BaseCommand):
    
    help = 'Export The DATA OF The Desired Table Into CSV FILE....'

    def add_arguments(self,parser):
        
        parser.add_argument('model_name',type=str,help='Enter Model Name')

    def handle(self,*args,**kwargs):
        
        timespam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        model_name = kwargs['model_name'].capitalize()
        file_path = f'Exported_Data_from_{model_name}_table_{timespam}.csv'
        model = None
        with open(file_path,'w') as file:
            for app_config in apps.get_app_configs():
                try:
                    model = apps.get_model(app_config.label,model_name)
                    break
                except LookupError:
                    continue
            if not model:
                self.stderr.write(f'model with model name {model_name} not found...')
            Data = model.objects.all()
            writer = csv.writer(file)
            writer.writerow([field.name for field in model._meta.fields])
            for dt in Data:
                writer.writerow([getattr(dt,field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS('Data Exported Successfully......'))


