from dataclasses import fields
from pyexpat import model
from turtle import width
from django import forms
from .models import Post
from .models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('author','title','content','image','is_twitter','is_facebook','is_instagram','created_date')
        widgets ={
            'author':forms.Select(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'created_date':forms.DateTimeInput(attrs={'class':'form-control'}),
        }
       
        def __init__(self,*args,**kwargs):
            super(PostForm,self).__init__(*args,**kwargs)
        

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','contactno','email','username','password1','password2')
        fields_required=('first_name','last_name','contactno','email','username','password1','password2')
    
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text=None

