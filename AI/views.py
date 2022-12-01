from django.http import HttpResponse
from django.shortcuts import render
import os
import openai
dark= False
openai.api_key = "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"
mk = "Hey 🤩, You've found who created the Site 😇"
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
def ind():
    b=str()
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
        if b == "mukesh" or b=="MUKESH" or b=="Mukesh":
            fir = mk
        else:
            fir = response['choices'][0]['text']
    except:
        pass
    c=cr
    return c,fir,b
def index(request):
    c,fir,b=ind()
    return render(request,'index.html',{'quto':c,'fir':fir,'ct':b,'dark':dark})
def GC(request):
    b=str()
    fir = """ """
    try:
        b = request.POST['topic']
        a = "Correct this to standard English:"
        if b == "mukesh" or b=="MUKESH" or b=="Mukesh":
            fir = mk
        else:
            fir=engine(a,b)
        print(fir)
    except:
        print("passed")
        pass
    c=cr
    return render(request,'gc.html',{'quto':c,'fir':fir,'ct':b})
def emoji(request):
    b=str()
    fir = str()
    try:
        b = request.POST['topic']
        a = "Convert into emoji"
        if b == "mukesh" or b=="MUKESH" or b=="Mukesh":
            fir = mk
        else:
            fir=engine(a,b)
        print(fir)
    except:
        print("passed")
        pass
    c=cr
    return render(request,'emoji.html',{'quto':c,'fir':fir,'ct':b})
def quest(request):
    b=str()
    fir = str()
    try:
        b = request.POST['topic']
        a = "what is "
        if b == "mukesh" or b=="MUKESH" or b=="Mukesh":
            fir = mk
        else:
            fir=engine(a,b)
        print(fir)
    except:
        print("passed tis")
        pass
    c=cr
    return render(request,'quest.html',{'quto':c,'fir':fir,'ct':b})
def quote(request):
    b=str()
    fir = str()
    try:
        b = request.POST['topic']
        a = "Write Quote for "
        if b == "mukesh" or b=="MUKESH" or b=="Mukesh":
            fir = mk
        else:
            fir=engine(a,b)
        print(fir)
    except:
        print("passed tis")
        pass
    c=cr
    return render(request,'quote.html',{'quto':c,'fir':fir,'ct':b}) 
def bl(request):
    global dark
    dark=False
    c,fir,b=ind()
    return render(request,'index.html',{'quto':c,'fir':fir,'ct':b,'dark':dark})
def wh(request):
    global dark
    dark=True
    c,fir,b=ind()
    return render(request,'index.html',{'quto':c,'fir':fir,'ct':b,'dark':dark})
def change(request):
  index(request)
