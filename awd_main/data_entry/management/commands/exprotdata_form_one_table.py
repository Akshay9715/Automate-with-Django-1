from django.core.management.base import BaseCommand
from data_entry.models import Student
import csv
import datetime


class Command(BaseCommand):

    def add_arguments(self, parser):
        help= 'Export DATA from a Table into CSV file.'

    def handle(self,*args,**kwargs):
        Data = Student.objects.all()
        timespam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_path = f'Exported_data_{timespam}.csv'
        print(file_path)
        with open(file_path,'w') as file:
            writer = csv.writer(file)
            writer.writerow(['roll_no','name','age'])
            for student in Data:
                writer.writerow([student.roll_no,student.name,student.age])

        self.stdout.write(self.style.SUCCESS('DATA Exported SUCCESSFULLY....'))