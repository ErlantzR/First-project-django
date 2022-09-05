from django.http import HttpResponse
import datetime

def greeting(request):

    return HttpResponse("Hello World!")

def goodbye(request):

    return HttpResponse("Good Bye! Have a nice day")


def date(request):

    current_date = datetime.datetime.now()
    document = f"Current date: {current_date}"
    return HttpResponse(document)

def age_calculator(request, year, current_age):

    passed_time = year - 2022
    future_age = current_age + passed_time
    document = f"In year {year} you will be {future_age} years old"

    return HttpResponse(document)