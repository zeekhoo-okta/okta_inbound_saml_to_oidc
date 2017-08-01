from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html')


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


@csrf_exempt
def oauth_callback(request):
    print('do callback request = {}'.format(request.POST))
    return render(request, 'callback.html')


def fb_callback(request):
    print('fb callback')
    return render(request, 'callback.html')


def saml_callback(request):
    if request.method == 'POST':
        print(request.body)
