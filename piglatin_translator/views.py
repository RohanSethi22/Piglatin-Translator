from django.http import HttpResponse
from django.shortcuts import render

def hellopage(request):
	return HttpResponse('<h1>Hello World!</h1>')

def homepage(request):
	return render(request,'home.html')

def translate_consonant(word):
    translation=''
    i=0
    vowel=False
    for i,letter in enumerate(word):
        if letter in 'aeiou':
        	vowel=True
        	break
    if vowel==False:
    	i+=1
    translation=word[i:]+word[0:i]+'ay'
    return translation

def transpage(request):
    text=request.GET['original_text'].lower()
    translated_text=''
    for word in text.split():
        if word[0] in 'aeiou':
            translated_text+=word+'way '
        else:
            translated_text+=translate_consonant(word)+' '
    return render(request,'tpage.html',{'original':text, 'translation': translated_text})

def aboutpage(request):
	return render(request,'about.html')