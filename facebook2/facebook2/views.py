from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Hello World!</h1>')

def profile(request):
    return HttpResponse('<h2>Md Monirozzaman</h2>')

def post(request):
    return HttpResponse('<h2>Good Morning Bangladesh</h2>') 

def notice(request, id=1):
    return HttpResponse('<h2>You are seeing Notice: '+ str(id) +' </h2>')       