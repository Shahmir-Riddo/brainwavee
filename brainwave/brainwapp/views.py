from django.shortcuts import render, HttpResponse
import openai
import re
from django.contrib import messages
from .models import Contact, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from googletrans import Translator
from brainwavee import *


translator = Translator()


api_keyy = ("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")
# Create your views here.
# Create your views here.


    

def index(request):
    return render(request, 'index.html')

def blogwriter(request):
    ans = ""
    if request.method == "POST":


    
        topic = request.POST.get('topic')
        title = request.POST.get('title')
        keyword = request.POST.get('keyword')
        lang =  request.POST.get('lang')
        tone = request.POST.get('tone')

        api_data = api_keyy
        openai.api_key = api_data


        completion = openai.Completion()

    
        prompt = (f"Generate a blog with {{tone}} tone of voice for the provided blog topic, title and keyword  title {title}  topic {topic} keyword {keyword}")
        response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
        answer = response.choices[0].text.strip()
        result = translator.translate(f'{answer}', dest=f'{lang}')
        ans = blogwave(result.text)
        
        
    context = {"ans": ans}
    return render(request, 'blogwriter.html', context)

def productdescwriter(request):
    ans = ""
    if request.method == "POST":


    
        name = request.POST.get('name')
        category = request.POST.get('category')
        keyword = request.POST.get('keyword')
        lang =  request.POST.get('lang')
        tone = request.POST.get('tone')
       
        api_data = api_keyy
        openai.api_key = api_data


        completion = openai.Completion()

    
        prompt = (f"Generate a product advertisement with {{tone}} tone of voice for the provided product name, category, features  product name {name}  category{category}  feature {keyword}")
        response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
        answer = response.choices[0].text.strip()
        result = translator.translate(f'{answer}', dest=f'{lang}')
    
        ans = adify(result.text)
        
        
    context = {"ans" : ans}
        
        
    return render(request, 'productdescwriter.html', context)

        
    


def paragenerator(request):
    ans = ""
    if request.method == "POST":

    
        name = request.POST.get('topic')
        
        keyword = request.POST.get('keyword')
        tone = request.POST.get('tone')

        lang = request.POST.get('lang')
        if lang == "bn":
                name = translator.translate(name)      
        api_data = api_keyy
        openai.api_key = api_data


        completion = openai.Completion()

    
        prompt = (f"Generate a application with {{tone}} tone of voice for the provided topic and keyword topic {name} keyword {keyword}")
        response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
        answer = response.choices[0].text
   
        
        
        result = translator.translate(f'{answer}', dest=f'{lang}')
   
        ans = result.text + ans
        
        
    context = {"ans" : ans}
    return render(request, 'paragenerator.html', context)

def emailgenerator(request):
    ans = ""
    if request.method == "POST":

    
        topic = request.POST.get('topic')
        keyword = request.POST.get('keyword')
        lang = request.POST.get('lang')
        if lang == "bn":
            topic = translator.translate(topic)
            topic = translator.translate(keyword)    
        api_data = api_keyy
        openai.api_key = api_data


        completion = openai.Completion()

    
        prompt = (f"Write a email for the provided topic and keyword, topic {topic} keyword {keyword}")
        response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
        answer = response.choices[0].text.strip()
        result = translator.translate(f'{answer}', dest=f'{lang}')
        ans = result.text + ans
        ans = adify(ans)
        
    context = {"ans" : ans}
        
        
    return render(request, 'jokesgenerator.html', context)



def lyricsgenerator(request):
    ans = ""
    if request.method == "POST":

    
        name = request.POST.get('name')
        keyword = request.POST.get('keyword')
        lang = request.POST.get('lang')
        genre = request.POST.get('genre')
        if lang == "bn":
            topic = translator.translate(name)
            topic = translator.translate(keyword)    
        api_data = api_keyy
        openai.api_key = api_data


        completion = openai.Completion()

    
        prompt = (f"Write a song lyrics for the provided name, genre and keyword, name {name}, genre {genre}, keyword {keyword}")
        response = completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=2048)
        answer = response.choices[0].text.strip()
        result = translator.translate(f'{answer}', dest=f'{lang}')
        ans = result.text + ans
        ans = adify(ans)
        
    context = {"ans" : ans}
        
        
    return render(request, 'lyricsgen.html', context)
def contact(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
    return render(request, 'contact.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

   
        user = authenticate(request, email=email, password=password)
        
        if user is not None:

            auth.login(request, user)
            return redirect("index")

    else:
        messages.info(request,  "Invalid Info")
        return render(request, "login.html")
    return render(request, 'login.html')

def createaccount(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email exists")

        
        else:

            
            user = User.objects.create_user(first_name=firstname,last_name=lastname, email=email, password= password)

            user.save()
            messages.info(request, "Registered Successfully")
            return redirect('profile/')
   



    return render(request, 'createaccount.html')

@login_required
def logout(request):
    logout(request)
    return  HttpResponseRedirect('/')

def items(request):
    return render(request, "items.html")
@login_required()
def profile(request):
    image = request.POST.get('image')
    bio = request.POST.get('bio')
    images = Profile(avatar=image)
    images.save
    context = {"bio": bio}
    return render(request, "profile.html")