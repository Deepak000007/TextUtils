# I have created this file
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

#code for personal navigator
# def index(request):
#     return HttpResponse('''<h1>hello</h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django code</a>''')

# def about(request):
#     return HttpResponse("about")

#code for pipe
def index(request):
    params = {'name': 'harry', 'place': 'Mars' }
    return render(request, 'index.html', params)
    #  return HttpResponse("Home")

def analyze(request):
    # print(request.GET.get('text', 'default'))
    #Get the text
    text = (request.POST.get('text', 'default'))

    #check checkbox values
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = (request.GET.get('fullcaps', 'off'))
    # 
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.GET.get('extraspaceremover', 'off'))
    print(removepunc)
    print(text)
    #analyze the text
    # return HttpResponse("analyze")
    # analyzed = text

    #check which checkbox is on
    if removepunc == "on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        # text = analyzed
        # return render(request, 'analyze.html', params)
        return render(request, 'analyze.html', params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed new Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1] == " "):
                analyzed = analyzed + char
            #or
            # if text[index] == " " and text[index+1] == " ": 
            #     pass
            # else:
            #     analyzed = analyzed + char
        params = {'purpose': 'Removed new Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else: 
        return HttpResponse("Error")

def removepunc(request):
    print(request.GET.get('text', 'default'))
    #Get the text
    text = (request.GET.get('text', 'default'))
    print(text)
    #analyze the text
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newlineremove first")

def spaceremove(request):
    return HttpResponse("spaceremove first <a href='/'>Back</a>")

def charcount(request):
    return HttpResponse("charcount first")