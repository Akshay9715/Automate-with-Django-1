from django.core.management.base import BaseCommand
from data_entry.models import Student
import csv


# command :- python manage.py insertdataCSV file_path

class Command(BaseCommand):


    help = "Takes csv file and load its data into DATABASE"

    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help="Enter File Path")

    def handle(self,*args,**kwargs):
        file_path = kwargs['file_path']
        with open(file_path,'r') as f:     
            reader = csv.DictReader(f)
            print(reader)
            for row in reader:
                # Student.objects.create(roll_no =row['roll_no'], age = row['age'],name = row['name'])
                Student.objects.create(**row)
        print(file_path)
        self.stdout.write(self.style.SUCCESS('Data Inserted SUCCESSFULLY.....'))