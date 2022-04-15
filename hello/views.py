
from string import punctuation
from this import d
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    m={'name':'Rajan','place':'USA'}
    return render(request,'index.html')

def rmp(request):
    djtext=request.POST.get('text', 'default')
    text=request.POST.get('rp', 'off')
    fullcap=request.POST.get('fullcap', 'off')
    rnl=request.POST.get('rnl', 'off')
    nc=request.POST.get('nc', 'off')
    
    if(text =="on"):
        punctuation=''':()-[]{};!'"\,<>?/~&*_'''
        analyze=""
        for char in djtext:
            if char not in punctuation:
                analyze = analyze + char
        perms= {'purpose':'Remove Puncutation','analyze_text':analyze}
        djtext=analyze
        
    if(fullcap=="on"):
        analyze=""
        for char in djtext:
            analyze=analyze + char.upper()
        perms= {'purpose':'Upercase','analyze_text':analyze}
        djtext=analyze
        
    if(rnl=="on"):
        analyze=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyze=analyze + char
        perms= {'purpose':'Remove new line','analyze_text':analyze}
        djtext=analyze
       
    if(nc=="on"):
        analyze=""
        for char in djtext:
            analyze=len(djtext)
        perms= {'purpose':'Number of character','analyze_text':analyze}
        
    if(text!="on" and fullcap!="on" and rnl!="on" and nc!="on"):
        return HttpResponse("error")
    
    return render(request,'analyze.html',perms)   