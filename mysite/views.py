#Self Made File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    gettext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(gettext)
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in gettext:
            if  char not in punctuations:
                analyze=analyze+char
        params={'purpose':'Removed Punctuations' , 'analyzed':analyze}
        return render(request,'analyze.html',params)


    else:
        return HttpResponse("<h1>Error</h1>")
