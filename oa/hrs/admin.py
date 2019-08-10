from django.contrib import admin

# Register your models here.
from hrs.models import Emp,Dept

class DeptAdmin(admin.ModelAdmin):
    list_display = ("no","name","location")
    ordering=("no",)
    def __str__(self):
        return self.name
class EmpAdmin(admin.ModelAdmin):
    list_display = ("no","name","job","mgr","sal","comm","dept")
    search_fields = ("name","job")
    def __str__(self):
        return self.name
admin.site.register(Dept,DeptAdmin)
admin.site.register(Emp,EmpAdmin)
