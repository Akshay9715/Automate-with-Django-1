from django.contrib import admin
from .models import Student,Customer,Uploads

# Register your models here.

class UploadAdmin(admin.ModelAdmin):
    list_display = ['model_name','uploaded_at']

admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Uploads,UploadAdmin)







# User = Admin
# password = Admin123