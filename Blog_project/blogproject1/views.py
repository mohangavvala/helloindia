from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'testapp/home.html')
def Home2(request):
    return render(request,'testapp/index.html')
def Home4(request):
    return render(request,'testapp/blog-single.html')