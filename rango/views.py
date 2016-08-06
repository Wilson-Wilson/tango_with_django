from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    # you could've also just put the value there instead of creating a variable
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("Rango says here's the about page. <br/> <a href='/rango/'>Index</a>")
