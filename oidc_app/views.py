from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def oauth_auth(request):
    print('do auth')

    client_id = settings.CLIENT_ID
    okta_org = settings.OKTA_ORG
    redirect_uri = settings.REDIRECT_URI

    c = {
        "client_id": client_id,
        "okta_org": okta_org,
        "redirect_uri": redirect_uri
    }
    return render(request, 'authorize.html', c)


def oauth_callback(request):
    print('do callback')
    return render(request, 'callback.html')


def fb_callback(request):
    print('fb callback')
    return render(request, 'callback.html')
