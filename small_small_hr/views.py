from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import ApplyLeaveForm, ApplyOverTimeForm

# Create your views here.


@login_required
def ApplyLeave(request):
    if request.method == 'POST':
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            form.super().save()
            leave_application_email(leave_obj=leave)
            messages.success(request, f'Your annual leave application has been submitted successfully, kindly wait for approval')
            return redirect('home')
    else:
        form = ApplyLeaveForm()
    return render(request, 'small_small_hr/apply-leave.html', {'form': form})


@login_required
def ApplyOverTime(request):
    if request.method=='POST':
        form=ApplyOverTimeForm(request.POST)
        if form.is_valid():
            form.super().save()
            overtime_application_email(leave_obj=leave)
            messages.success(request, f'Your overtime application has been submitted successfully, kindly wait for approval')
            return redirect('home')
    else:
        form=ApplyOverTimeForm()
    return render(request, 'small_small_hr/apply-overtime.html', {'form': form})



# @user_passes_test(lambda u: u.is_superuser)
# def CreateStaff(request):
#     if request.method == 'POST':
#         form = StaffProfileAdminCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Staff created successfully')
#             return redirect('home')
#     else:
#         form = StaffProfileAdminCreateForm()
#     return render(request, 'small_small_hr/create-staff.html', {'form': form})


# @user_passes_test(lambda u: u.is_superuser)
# def ManageAnnualLeave(request):
#     if request.method=='POST':
#         form=AnnualLeaveForm(request.POSt)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'form editted successfully')
#             return redirect('home')
#     else:
#         form=AnnualLeaveForm()
#     return render(request, 'small_small_hr/annual-leave.html', {'form':form})




# @user_passes_test(lambda u: u.is_superuser)
# def ManageRoles(request):
#     if request.method=='POST':
#         form=RoleForm(request.POSt)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Role saved successfully')
#             return redirect('home')
#     else:
#         form=RoleForm()
#     return render(request, 'small_small_hr/role-form.html', {'form':form})

  

# @user_passes_test(lambda u: u.is_superuser)
# def ManageHolidays(request):
#     if request.method=='POST':
#         form=HolidayDayForm(request.POSt)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Holiday saved successfully')
#             return redirect('home')
#     else:
#         form=HolidayDayForm()
#     return render(request, 'small_small_hr/holiday-form.html', {'form':form})


# @user_passes_test(lambda u: u.is_superuser)
# def ManageOvertime(request):
#     if request.method=='POST':
#         form=OverTimeForm(request.POSt)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Sucess')
#             return redirect('home')
#     else:
#         form=OverTimeForm()
#     return render(request, 'small_small_hr/overtime-form.html', {'form':form})


# @user_passes_test(lambda u: u.is_superuser)
# def ManageLeave(request):
#     if request.method=='POST':
#         form=LeaveForm(request.POSt)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Sucess')
#             return redirect('home')
#     else:
#         form=LeaveForm()
#     return render(request, 'small_small_hr/leave-form.html', {'form':form})



# @user_passes_test(lambda u: u.is_superuser)
# def StaffDocuments(request):
#     if request.method=='POST':
#         form=StaffDocumentForm(request.POSt)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Sucess')
#             return redirect('home')
#     else:
#         form=StaffDocumentForm()
#     return render(request, 'small_small_hr/staff-docs.html', {'form':form})



# @user_passes_test(lambda u: u.is_superuser)
# def StaffProfiles(request):
#     if request.method=='POST':
#         form=StaffProfileAdminForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Sucess')
#             return redirect('home')
#     else:
#         form=StaffProfileAdminForm()
#     return render(request, 'small_small_hr/staff-profiles.html', {'form':form})




