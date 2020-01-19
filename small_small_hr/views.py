from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import ApplyLeaveForm, StaffProfileAdminCreateForm, AnnualLeaveForm, RoleForm, HolidayDayForm

# Create your views here.


@login_required
def ApplyLeave(request):
    if request.method == 'POST':
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your annual leave application has been submitted successfully')
            return redirect('home')
    else:
        form = ApplyLeaveForm()
    return render(request, 'small_small_hr/apply-leave.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def CreateStaff(request):
    if request.method == 'POST':
        form = StaffProfileAdminCreateForm(request.POST)
        if form.is_valid():
            form.save()
            pin_number=form.cleaned_data.get('PIN Number')
            messages.success(request, f'Staff created successfully')
            return redirect('home')
    else:
        form = StaffProfileAdminCreateForm()
    return render(request, 'small_small_hr/create-staff.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def ManageAnnualLeave(request):
    if request.method=='POST':
        form=AnnualLeaveForm(request.POSt)
        if form.is_valid():
            form.save()
            messages.success(request, f'form editted successfully')
            return redirect('home')
    else:
        form=AnnualLeaveForm()
    return render(request, 'small_small_hr/annual-leave.html', {'form':form})




@user_passes_test(lambda u: u.is_superuser)
def ManageRoles(request):
    if request.method=='POST':
        form=RoleForm(request.POSt)
        if form.is_valid():
            form.save()
            messages.success(request, f'Role saved successfully')
            return redirect('home')
    else:
        form=RoleForm()
    return render(request, 'small_small_hr/role-form.html', {'form':form})





  

@user_passes_test(lambda u: u.is_superuser)
def ManageHolidays(request):
    if request.method=='POST':
        form=HolidayDayForm(request.POSt)
        if form.is_valid():
            form.save()
            messages.success(request, f'Holiday saved successfully')
            return redirect('home')
    else:
        form=HolidayDayForm()
    return render(request, 'small_small_hr/holiday-form.html', {'form':form})