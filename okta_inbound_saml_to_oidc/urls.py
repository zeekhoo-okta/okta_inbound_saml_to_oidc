"""okta_inbound_saml_to_oidc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from oidc_app.views import home, oauth_auth, oauth_callback, fb_callback

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^oauth/authorize/$', oauth_auth, name='auth'),
    url(r'^oauth/callback/$', oauth_callback, name='callback'),
    url(r'^fb/callback/$', fb_callback, name='fb'),

]
