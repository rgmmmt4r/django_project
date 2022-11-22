from django.shortcuts import render
from django.http import HttpResponse
from .models import Testresult
from datetime import datetime, timedelta
from .form import DateForm
import pandas as pd
from django.utils import timezone

# Create your views here.

def index(request):
    startDate = timezone.localdate()
    endDate = startDate + timedelta(days=1)
    if request.method == "GET":
        form = DateForm()
    elif request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            startDate = form.cleaned_data['date']
            if form.cleaned_data['date2'] != None:               
                endDate = form.cleaned_data['date2'] + timedelta(days=1)
            else:
                endDate = startDate + timedelta(days=1)
    intervalDate = endDate - startDate
    result ={"id":"順序","dateTime":"日期時間",'result':'結果'}
    data = Testresult.objects.filter(dateTime__gte=startDate,dateTime__lte = endDate).values()
    df = pd.DataFrame(list(data))
    df = df.rename(result, axis='columns')
    return render(request, 'user/index.html', 
    {   
        'df':df,
        'startDate': startDate,
        'endDate':endDate,
        'form':form
    })