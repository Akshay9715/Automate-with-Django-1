from django.core.management.base import BaseCommand, CommandParser
from data_entry.models import Student


class Command(BaseCommand):
    

    def add_arguments(self,parser):
        parser.add_argument('roll_no', type=str,help='Enter roll no.')
        parser.add_argument('name',type=str,help='Enter Name')
        parser.add_argument('age',type=int,help='Enter the AGE')

    def handle(self,*args,**kwargs):

        roll_no = kwargs['roll_no']
        name = kwargs['name']
        age = kwargs['age']
        
        Student.objects.create(roll_no=roll_no,name=name,age=age)

        self.stdout.write(self.style.SUCCESS('Data Inserted Successfully....'))