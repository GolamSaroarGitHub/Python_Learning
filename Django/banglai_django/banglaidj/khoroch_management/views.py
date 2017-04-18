from django.shortcuts import render
from .models import Expenses


def my_expenses(request):

    expenses=Expenses.objects.all()
    context={'expenses':expenses}

    return render(request,'cost/khoroch.html',context)



# Create your views here.
