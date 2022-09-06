from django.http import HttpResponse
import datetime
from django.template import Template, Context

def greeting(request):

    name = "Erlantz"

    external_doc=open("/Users/erlantzramossanchez/Projects/Django/tutorial/tutorial/templates/my_greeting.html")

    tpl=Template(external_doc.read())

    external_doc.close()

    ctx=Context({"my_name": name})

    document=tpl.render(ctx)

    return HttpResponse(document)

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