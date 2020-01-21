from django.contrib import admin
from .models import Role,StaffProfile,StaffDocument,Leave,OverTime,AnnualLeave,FreeDay, Profile

# Register your models here.



admin.site.register(Role)
admin.site.register(StaffProfile)
admin.site.register(StaffDocument)
admin.site.register(Leave)
admin.site.register(OverTime)
admin.site.register(AnnualLeave)
admin.site.register(FreeDay)
admin.site.register(Profile)
