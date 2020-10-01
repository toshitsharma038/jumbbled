from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
from django.views.decorators.csrf import csrf_exempt,csrf_protect

words=["react","java","flutter","javascript"]



def index(request):
    return render(request,'index.html')

def rword():
    global jword
    global word
    word = random.choice(words)
    jum = random.sample(word,len(word))
    jword = "".join(jum)

msgs=""

def homepage(request):
    rword()
    global jword,msgs
    return render(request,'homepage.html',{'msg':jword,'msgs':msgs})

def checkans(request):
    global word,msgs,jword
    user_answer = request.GET.get('answer', True)
    if user_answer == word:
        msgs = "that was a correct answer"
        homepage(request)
    else:
        msgs = "Wrong answer"
    return render(request,'homepage.html',{'msg':jword,'msgs':msgs})
