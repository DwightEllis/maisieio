from django.shortcuts import render, get_object_or_404, redirect
from .models import IO
from .forms import IOForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def IO_list(request):
	ios = IO.objects.all().order_by('-event_date')
	return render(request, 'IO_Tracker/IO_list.html', {'ios':ios})

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