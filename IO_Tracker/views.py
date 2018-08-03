from django.shortcuts import render
from .models import IO

# Create your views here.
def IO_list(request):
	ios = IO.objects.all().order_by('event_date')
	return render(request, 'IO_Tracker/IO_list.html', {'ios':ios})