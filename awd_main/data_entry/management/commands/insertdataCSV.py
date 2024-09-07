from django.core.management.base import BaseCommand, CommandError
# from data_entry.models import Student, Customer
from django.apps import apps
import csv
from django.db import DataError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("file_name",type=str,help="Enter the file path here....")
        parser.add_argument("model_name",type=str,help="Enter the Model name...")

    def handle(self,*args,**kwargs):
        file_name = kwargs['file_name']
        model_name = kwargs['model_name'].capitalize()
        print(model_name)
        model = None

        for app in apps.get_app_configs():
            try:
                model = apps.get_model(app.label,model_name)
                break
            except LookupError:
                continue
        
        if not model:
            raise CommandError(f'Model with name {model_name} is NOT Present!!!')
        
        model_fields = [fields.name for fields in model._meta.fields if fields.name != 'id']
        

        with open(file_name,'r') as f:
            reader = csv.DictReader(f)
            csv_header = reader.fieldnames
            
            if csv_header != model_fields:
                raise DataError(f"CSV file does't match with the {model_name} table fields. ")

            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data Inserted SUCCESSFULLY...'))