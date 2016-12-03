from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def oauth_auth(request):
    print('do auth')
    return render(request, 'authorize.html')


def oauth_callback(request):
    print('do callback')
    return render(request, 'callback.html')


def fb_callback(request):
    print('fb callback')
    return render(request, 'callback.html')
