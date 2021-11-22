from django.shortcuts import render

# Create your views here.

# request
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    context={
        'name':'click it please!'
    }
    #return  HttpResponse('OK')
    return render(request,'book/index.html',context=context)