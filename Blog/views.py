from asyncio.windows_events import NULL
from email import message
from genericpath import exists
from gettext import NullTranslations
from multiprocessing import context
from xmlrpc.client import APPLICATION_ERROR
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from pkg_resources import NullProvider
from .models import *
from django.contrib import messages
from .models import Post
from django.views.generic import CreateView,UpdateView
from .form import PostForm,SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
import tweepy
from django.conf import settings
from instabot import Bot
import os
import glob
from pathlib import Path
import facebook as fb
 # Create your views here.

def home(request):
    loginform = AuthenticationForm()
    form=SignUpForm()
    if request.method=='POST':
       form=SignUpForm(request.POST)
       loginform=AuthenticationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,'Thanks for signing up. Welcome to our community.')
           return redirect('home')
       elif loginform.is_valid:
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect('userhome')
            else:
                return redirect('home') 
    context={'signupform':form, 'loginform':loginform}
    return render(request,'home.html', context)
    
def contact(request):
    return render(request,'contact.html')

def userhome(request):
    return render(request,'userhome.html')

# class AddPostView(CreateView):
#     model=Post
#     template_name='addpost.html'
#     form_class=PostForm
    
def addpost(request,id):
    form=PostForm()
    user=User.objects.get(id=id)
    api_key=user.twitter_api_key
    api_key_secret =user.twitter_api_key_secret
    access_token=user.twitter_access_token
    access_token_secret=user.twitter_access_token_secret
    facebook_access=user.facebook_access_token
    username=user.insta_username
    password=user.insta_password
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            status=request.POST.get('content')
            image = request.FILES['image']
            form.save()
            obj = form.instance 
            is_twitter = request.POST.get("is_twitter", None)
            is_facebook = request.POST.get("is_facebook", None)
            is_instagram = request.POST.get("is_instagram", None)
            print(is_twitter)
            print(is_facebook)
            print(is_instagram)

            # if is_twitter=='on':
            #     auth = tweepy.OAuthHandler(api_key,api_key_secret)
            #     auth.set_access_token(access_token,access_token_secret)
            #     api = tweepy.API(auth)
            #     imageurl = obj.imageurl.strip("/")
            #     media = api.media_upload(imageurl)
            #     api.update_status(status=status, media_ids=[media.media_id])
                
            #     messages.success(request,'Your Blog has been send Successfully!')
            #     return redirect('userhome')
            # if is_facebook=='on':
                
            #     asfab=fb.GraphAPI(facebook_access)
              
            #     imageurl = obj.imageurl.strip("/")
            #     print(imageurl)
            #     asfab.put_photo(open(imageurl,"rb"),message=status)
               
            #     return redirect('userhome')
            
            # if is_instagram=='on': 
            #     print("+++++++++++++++++++++++++")
            #     location = glob.glob("config/*cookie.json")
            #     print(location)
            #     location2 =''.join([str(item) for item in location])
            #     print(location2)
            #     if os.path.isfile(location2):
            #         os.remove(location2)
            #     print(username)
            #     print(password)
            #     print(image)
            #     imageurl = obj.imageurl.strip("/")
            #     bot=Bot()
            #     bot.login(username=username,password=password,is_threaded=True)
                
            #     bot.upload_photo(imageurl,caption=status)
                
            #     return redirect('userhome')
            
            if ((is_twitter=='on')| (is_facebook=='on') | (is_instagram=='on')):
                
                try:
                    if is_twitter=='on':
                        auth = tweepy.OAuthHandler(api_key,api_key_secret)
                        auth.set_access_token(access_token,access_token_secret)
                        api = tweepy.API(auth)
                        imageurl = obj.imageurl.strip("/")
                        media = api.media_upload(imageurl)
                        api.update_status(status=status, media_ids=[media.media_id])
                except:
                    messages.warning(request,'Your API Keys are expired.Please Update!')

                try:

                    if is_facebook=='on':
                        asfab=fb.GraphAPI(facebook_access)
                        imageurl = obj.imageurl.strip("/")
                        print(imageurl)
                        asfab.put_photo(open(imageurl,"rb"),message=status)
                except:
                    messages.warning(request,'Your Access tokens are expired.Please Update!')

                try:

                    if is_instagram=='on': 

                        location = glob.glob("config/*cookie.json")
                        print(location)
                        location2 =''.join([str(item) for item in location])
                        print(location2)
                        if os.path.isfile(location2):
                            os.remove(location2)
                        print(username)
                        print(password)
                        print(image)
                        imageurl = obj.imageurl.strip("/")
                        bot=Bot()
                        bot.login(username=username,password=password,is_threaded=True)
                    
                        bot.upload_photo(imageurl,caption=status)
                except:
                    messages.warning(request,'Sorry Its for server down Issues.Try again!')
            # return redirect('userhome')
            return render(request,'addpost.html',{'form':form})
            
    return render(request,'addpost.html',{'form':form})

def editprofile(request,id):
   
    user=User.objects.get(id=id)
    return render(request,'editprofile.html',{'user':user})

def update(request,id):
    if request.method == "POST":
        user=User.objects.get(id=id)
        user.email=request.POST.get('txtemail')
        user.contactno=request.POST.get('txtcontactno')
        user.username=request.POST.get('txtusername')
        user.twitter_api_key=request.POST.get('txtapikey')
        user.twitter_api_key_secret=request.POST.get('txtapikeysecret')
        user.twitter_access_token=request.POST.get('txtaccesstoken')
        user.twitter_access_token_secret=request.POST.get('txtaccesstokensecret')
        user.insta_username=request.POST.get('txtinstausername')
        user.insta_password=request.POST.get('txtinstapassword')
        user.facebook_access_token=request.POST.get('txtfacebookaccess')
        user.save()
        print(user.id)
        
    return redirect('userhome')

def doc(request):
    return render(request,'doc.html')


