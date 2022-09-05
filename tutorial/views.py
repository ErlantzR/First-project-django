from django.http import HttpResponse

def greeting(request):

    return HttpResponse("Hello World!")

def goodbye(request):

    return HttpResponse("Good Bye! Have a nice day")