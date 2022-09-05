from django.http import HttpResponse
import datetime

def greeting(request):

    return HttpResponse("Hello World!")

def goodbye(request):

    return HttpResponse("Good Bye! Have a nice day")


def date(request):

    current_date = datetime.datetime.now()
    document = f"Current date {current_date}"
    return HttpResponse(document)