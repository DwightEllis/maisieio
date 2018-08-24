from django.shortcuts import render, get_object_or_404, redirect
from .models import IO
from .forms import IOForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Sum
from django.template import Library
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
    """ First parameterize the query by day, so that way you don't 
    have massive tables. 

    By default, it shows today, but http://website/daily_summary?date=2018-07-21
    will show July 21st
    """
    date = request.GET.get('date', None)
    if date is None:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    """ Lets actually make several queries by iterating over all the hours in the day 
    Save the results for each hour in the 'data' object indexed by the hour
    """
    hours = range(1, 25)
    data = {}
    for hour in hours:
        data[hour] = IO.objects.filter(
            event_date__date=date,event_date__hour=hour
        ).values('input_type').annotate(Sum('quantity'))

    """ Fetch all the possible input_types from the DB. This will allow us to automatically
    create the table based on available data. If you know all the input types you'll ever 
    see, this isn't necessary and does simplify some things."""
    input_types = IO.objects.values('input_type').distinct('input_type').all()

    """ Send back a dataset that contains our actual aggregated quantities indexed by hour,
     the set of input types we have, the date that this query had, and the hours in the day"""
    response = {
        "input_types": input_types,
        "date": date,
        "hours": list(hours),
        "data": data
    }
    return render(request, 'IO_Tracker/daily_summary.html', response)

    all_events = IO.objects.filter(event_date__date=date).all()

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