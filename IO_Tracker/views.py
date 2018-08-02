from django.shortcuts import render

# Create your views here.
def IO_list(request):
    return render(request, 'IO_Tracker/IO_list.html', {})