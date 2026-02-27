# records/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUpForm, RecordForm
from .models import Record


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('record_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'records/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect('record_list')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'records/login.html')


def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required
def record_list(request):
    records = Record.objects.filter(user=request.user)
    return render(request, 'records/record_list.html', {'records': records})


@login_required
def record_create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, "Record created successfully!")
            return redirect('record_list')
    else:
        form = RecordForm()

    return render(request, 'records/record_form.html', {
        'form': form,
        'title': 'Add New Record'
    })


@login_required
def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk, user=request.user)

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)

    return render(request, 'records/record_form.html', {
        'form': form,
        'title': 'Edit Record'
    })


@login_required
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk, user=request.user)

    if request.method == 'POST':
        record.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('record_list')

    return render(request, 'records/record_confirm_delete.html', {'record': record})