from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "<html><body><h1>Hello!</h1> <br> \
             <h3>Please go to <b><a href=\"/admin\">admin</a></b> page.</h3> <br> </body></html>"
    return HttpResponse(html)
