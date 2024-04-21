from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/index.html')

def contacts(request):
    return render(request, 'contacts/index.html')
# Create your views here.
