from django.shortcuts import render

# Create your views here.
def login(request):
    return render(
        request=request,
        template_name='GamifApp/login.html',
        context={},
    )
def signup(request):
    return render(
        request=request,
        template_name='GamifApp/signup.html',
        context={},
    )
