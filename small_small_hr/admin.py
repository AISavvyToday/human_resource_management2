from django.contrib import admin
from .models import TimeStampedModel,Role,StaffProfile,StaffDocument,BaseStaffRequest,Leave,OverTime,AnnualLeave,FreeDay

# Register your models here.



admin.site.register(Role)
admin.site.register(StaffProfile)
admin.site.register(StaffDocument)
admin.site.register(Leave)
admin.site.register(OverTime)
admin.site.register(AnnualLeave)
admin.site.register(FreeDay)