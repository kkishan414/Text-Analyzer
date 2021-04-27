# I have created this file - Kishan kumar
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
    # return HttpResponse('home')

def analyze(request):
    djtext = request.POST.get('text','default')# text

    # check check box
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    
    
    if removepunc == "on":   # checking remove punctuation
        punctuations = '''!()-[]{};:'"/,<>.\@#$%^&*-_~?'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed += i
        params = {'purpose':"Remove Punctuations",'analyzed_text' : analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        for i in djtext:
            analyzed = analyzed + i.upper()
        params = {'purpose':"Changed to Uppercase",'analyzed_text' : analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for i in djtext:
            if i != '\n' and i != '\r':
                analyzed = analyzed + i
        params = {'purpose':"Removed New Lines",'analyzed_text' : analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        djtext1 = ''
        k = len(djtext) - 1 
        while(k >= 0):
            if djtext[k] != " ":
                for i in range(k+1):
                    djtext1 = djtext1 + djtext[i]
                break 
            k -= 1

        for i,char in enumerate(djtext1):
            if not(djtext1[i] == ' ' and djtext[i+1] == ' ' )  :
                analyzed = analyzed + char
        params = {'purpose':"Extra Space Removed",'analyzed_text' : analyzed}
        djtext = analyzed
    
    if charcount == 'on':
        analyzed = djtext +f'\n [Total character is {len(djtext)}]'
        params = {'purpose':"Counting Character",'analyzed_text' : analyzed}  
            
    
    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on' : 
        analyzed = djtext
        params = {'purpose':"No Changes",'analyzed_text' : analyzed}  
    
    return render(request,'analyze.html',params)

