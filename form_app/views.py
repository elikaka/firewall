from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import FormData

def form_view(request):
    return render(request, 'form_template.html')

def form_submission(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        form_data = FormData(username=username, password=password)
        form_data.save()

        return HttpResponse('Form submitted and data saved to the database!')
    else:
        return HttpResponse('Method not allowed')