from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    my_context = {'username': 'Axel',
                  'minecraft': 'jugar minecraft',
                  'dormir': 'dormir sin tareas',
                  'programar': 'me gusta programar'}

    return render(request,'mi_chamba/index.html',context=my_context)
    
    #return HttpResponse("Hello Word")