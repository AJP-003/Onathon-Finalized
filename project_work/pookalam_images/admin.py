from django.contrib import admin
from .models import Tables

# Register your models here.





class TablesAdmin(admin.ModelAdmin):
    list_display = ("image","red","yellow","white","orange","violet","green","pink")


admin.site.register(Tables,TablesAdmin)