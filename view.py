from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analysis(request):
    djtext=request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    capitalise=request.POST.get('capitalise','off')
    newlineremover=request.POST.get('newlineremover','off')
    charactercount=request.POST.get('charactercount','off')
    print(removepunc)
    print(djtext)


    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysedtext=''
        for char in djtext:
            if char not in punctuations:
                analysedtext=analysedtext+char

        params = {'purpose': 'Remove Punctuations', 'analysedtext': analysedtext}
        djtext=analysedtext

    if capitalise == 'on':
        analysedtext=''
        for char in djtext:
            analysedtext=analysedtext+char.upper()
        params={'purpose':'Capitalise Text','analysedtext':analysedtext}
        djtext=analysedtext

    if newlineremover == 'on':
        analysedtext=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analysedtext=analysedtext+char

        params={'purpose':'New Line Remover','analysedtext':analysedtext}

    if charactercount == 'on':
        analysedtext = 0
        for char in djtext:
            if char.isalpha():
                analsedtext = analysedtext + 1

    if(removepunc!='on' and capitalise!='on' and newlineremover!='on'):
        return HttpResponse("Error")

    return render(request,'analysis.html',params)

