from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def analyze(request):
    intext=request.POST.get('text','default')
    punc_switch=request.POST.get('puncswitch','off')
    cap_switch=request.POST.get('capswitch','off')
    line_switch=request.POST.get('lineswitch','off')
    space_switch=request.POST.get('spaceswitch','off')
    count_switch=request.POST.get('countswitch','off')
    # print(intext)
    # print(punc_swtch)
    
    if punc_switch == 'on':
        pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_txt=""
        ertext=""
        
        for char in intext:
            if char not in pun:
                 analyzed_txt+=char 
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed_txt}
        intext=analyzed_txt
        # return render(request,"analyze.html",params)

    if (cap_switch=='on'):
        analyzed=""
        for char in intext:
            analyzed+=char.upper()
        params={'purpose':'Upper Case ', 'analyzed_text':analyzed}
        intext=analyzed
        # return render(request,"analyze.html",params)

    if (line_switch=='on'):
        analyzed=""
        for char in intext:
            if char !="\n" and char!='\r':
                analyzed+=char
            
        params={'purpose':'New Line Removed ', 'analyzed_text':analyzed}
        intext=analyzed
        # return render(request,"analyze.html",params)

    if (space_switch=='on'):
        analyzed=""
        for index,char in enumerate(intext):
            if not(intext[index]==" "and intext[index+1]==" "):
                analyzed+=char
        params={'purpose':'Extra Space Removed ', 'analyzed_text':analyzed}
        intext=analyzed
        # return render(request,"analyze.html",params)
    
    if (count_switch=='on'):
        analyzed_count=len(intext)
        params_c={'purpose':'Total Characters ', 'analyzed_text_count':analyzed_count}
        # intext=analyzed
        return render(request,"analyze.html",params_c)
        

    else:
        
        ertext=intext
        error={'err1':':Please Switch On Checkbox', 'err2':ertext }
        return render(request,'analyze.html',error)

    return render(request,"analyze.html",params,params_c)

def bgchanger(request):
    return render(request,"background_changer.html")

def cheatsheet(request):
    return render(request,"cheatsheet.html")