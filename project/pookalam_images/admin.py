from django.contrib import admin
from .models import Pookal





class TablesAdmin(admin.ModelAdmin):
    list_display = ("image","red","yellow","white","orange","violet","green","pink")


# Register your models here.
admin.site.register(Pookal,TablesAdmin)