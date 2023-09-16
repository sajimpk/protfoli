from django.contrib import admin

# Register your models here.
from .models import contact
# Register your models here.
class showAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','message','time')

admin.site.register(contact,showAdmin)