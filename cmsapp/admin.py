from django.contrib import admin
from .models import DepartmentModel
from .models import StudentModel
from .models import SportModel
# Register your models here.

admin.site.register(DepartmentModel)
admin.site.register(StudentModel)
admin.site.register(SportModel)