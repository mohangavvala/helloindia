from django import forms
class EmailForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)#may be comments or maynot be comments so comment required=False

#comments form sections
from blog.models import comments
class commentform(forms.ModelForm):
    class Meta:
        model=comments
        fields=('name','email','body')
from blog.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        #author = forms.ModelChoiceField(queryset=Post.objects.all(),
        exclude = ['publish','status']                                #widget=forms.HiddenInput())
        fields="__all__"
        #exclude = ['author']
       # fields = ('title', 'slug')
from django import forms
from django.contrib.auth.models import User
class Signup_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']