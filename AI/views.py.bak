from django.http import HttpResponse
from django.shortcuts import render
import os
import openai
openai.api_key = "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"
respons = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Write a Random Quote",
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
text=respons['choices'][0]['text']
cr=text.replace('Generator', "")

def engine(a,b):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=a+":\n\n"+b,
            temperature=0.5,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
        fir = response['choices'][0]['text']
        return fir
def index(request):
    fir = """ """
    try:
        a=request.POST['topic']
        b=request.POST['ans']
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=a+":\n\n"+b,
            temperature=0.5,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
        fir = response['choices'][0]['text']
    except:
        pass
    c=cr
    return render(request,'index.html',{'quto':c,'fir':fir})
def GC(request):
    fir = """ """
    try:
        b = request.POST['topic']
        a = "Correct Sentence"
        fir=engine(a,b)
        print(fir)
    except:
        print("passed")
        pass
    c=cr
    return render(request,'gc.html',{'quto':c,'fir':fir})
def emoji(request):
    fir = str()
    try:
        b = request.POST['topic']
        a = "Convert into emoji"
        fir=engine(a,b)
        print(fir)
    except:
        print("passed")
        pass
    c=cr
    return render(request,'emoji.html',{'quto':c,'fir':fir})
def quest(request):
    fir = str()
    try:
        b = request.POST['topic']
        a = "what is "
        fir=engine(a,b)
        print(fir)
    except:
        print("passed tis")
        pass
    c=cr
    return render(request,'quest.html',{'quto':c,'fir':fir})
def quote(request):
    fir = str()
    try:
        b = request.POST['topic']
        a = "Write Quote for "
        fir=engine(a,b)
        print(fir)
    except:
        print("passed tis")
        pass
    c=cr
    return render(request,'quote.html',{'quto':c,'fir':fir})