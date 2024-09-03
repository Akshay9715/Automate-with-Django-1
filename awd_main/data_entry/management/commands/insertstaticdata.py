from typing import Any
from django.core.management.base import BaseCommand
from data_entry.models import Student


class Command(BaseCommand):


    help= 'This command will Insert Static Data'

    def handle(self,*agrs,**kwargs):

        data_set = [
        {
            'roll_no': '1001',
            'name':'Rahul',
            'age':20
        },
        {
            'roll_no': '1002',
            'name':'Rakesh',
            'age':21 
        },
        {
            'roll_no': '1003',
            'name':'Rajat',
            'age':19
        }
        ]
        for  data in data_set:
            present = None
            present = Student.objects.filter(roll_no=data['roll_no'])
            if not present:
                Student.objects.create(roll_no = data['roll_no'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with Roll No. {data['roll_no']} is already present.'))
        self.stdout.write(self.style.SUCCESS("Data inserted successfully...."))
