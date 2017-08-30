from django.shortcuts import render,redirect

from .models import Expenses
from .forms import ExpensesForm
def costs(request):
    expenses = Expenses.objects.all().order_by('-date')
    context = {
        'expenses' : expenses
    }

    return render(request,'costs/list.html',context)



def add_Expenses(request):

    if request.method=='POST':
        form=ExpensesForm(request.POST)
        form.save()
        return redirect('cost-list')

    else:
        form=ExpensesForm
    return render(request,'costs/add_expense.html',{'form':form})

