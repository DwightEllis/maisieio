from django.shortcuts import render, get_object_or_404, redirect
from .models import IO
from .forms import IOForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Sum
import datetime

# Create your views here.
@login_required
def IO_list(request):
    ios = IO.objects.all().order_by('-event_date')
    return render(request, 'IO_Tracker/IO_list.html', {'ios':ios})

@login_required
def trends(request):
    return render(request, 'IO_Tracker/trends.html', {})

@login_required
def daily_summary(request):
    testsum = IO.objects.filter(event_date__hour=23).values('input_type').annotate(Sum('quantity'))
    testsum17 = IO.objects.filter(event_date__hour=17,event_date__date=(datetime.date(2018,8,6))).values('input_type').annotate(Sum('quantity'))
    dailysum_TPN = IO.objects.filter(input_type='TPN').aggregate(Sum('quantity'))        
    dailysum_LIP = IO.objects.filter(input_type='LIP').aggregate(Sum('quantity'))
    dailysum_ENT = IO.objects.filter(input_type='ENT').aggregate(Sum('quantity'))
    dailysum_BOT = IO.objects.filter(input_type='BOT').aggregate(Sum('quantity'))
    dailysum_MED = IO.objects.filter(input_type='MED').aggregate(Sum('quantity'))
    dailysum_DIA = IO.objects.filter(input_type='DIA').aggregate(Sum('quantity'))
    dailysum_EME = IO.objects.filter(input_type='EME').aggregate(Sum('quantity'))
    dailysum_GAS = IO.objects.filter(input_type='GAS').aggregate(Sum('quantity'))
    return render(request, 'IO_Tracker/daily_summary.html', 
        {'dailysum_TPN':dailysum_TPN, 
        'dailysum_LIP': dailysum_LIP,
        'dailysum_ENT': dailysum_ENT,
        'dailysum_BOT': dailysum_BOT,
        'dailysum_MED': dailysum_MED,
        'dailysum_DIA': dailysum_DIA,
        'dailysum_EME': dailysum_EME,
        'dailysum_GAS': dailysum_GAS,
        'testsum': testsum,
        'testsum17': testsum17,
        })

@login_required
def io_new(request):
    if request.method == "POST":
        form = IOForm(request.POST)
        if form.is_valid():
            io = form.save(commit=False)
            io.user = request.user
            io.create_date = timezone.now()
            io.save()
            return redirect('/')
    else:
        form = IOForm()
    return render(request, 'IO_Tracker/io_edit.html', {'form': form})

@login_required
def io_edit(request, pk):
    io = get_object_or_404(IO, pk=pk)
    if request.method == "POST":
        form = IOForm(request.POST, instance=io)
        if form.is_valid():
            io = form.save(commit=False)
            io.user = request.user
            io.create_date = timezone.now()
            io.save()
            return redirect('/')
    else:
        form = IOForm(instance=io)
    return render(request, 'IO_Tracker/io_edit.html', {'form': form})

@login_required
def io_remove(request, pk):
    io = get_object_or_404(IO, pk=pk)
    io.delete()
    return redirect('/')