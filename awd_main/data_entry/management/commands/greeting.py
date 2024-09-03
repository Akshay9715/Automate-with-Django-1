from django.core.management.base import BaseCommand



class Command(BaseCommand):

    help = "It greets the user"

    def add_arguments(self,parser):
        parser.add_argument('name',type = str,help = 'Enter the Name')

    def handle(self,*args,**kwargs):
        name = kwargs['name']
        greeting = f'Hi, {name} Happy to see you!'
        self.stdout.write(greeting)
        self.stdout.write(self.style.ERROR(greeting))
        self.stdout.write(self.style.WARNING(greeting))
        self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(self.style.NOTICE(greeting))



# User = Admin
# password = Admin123