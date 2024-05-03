from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def getTimeInfo(request):
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    msg = '<h1>Hello Friends, '
    if hour < 12:
        msg = msg + 'Good Morning'
    elif hour < 16:
        msg = msg + 'Good Afternoon'
    elif hour < 21:
        msg = msg + 'Good Evening'
    else:
        msg = msg + 'Good Night'
    msg = msg + '</h1><hr>'
    msg = msg + '<h1>Now the server time is: ' +str(date) + '</h1>'
    print(msg)
    print(date)
    print(hour)
    return HttpResponse(msg)
