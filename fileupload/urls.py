"""fileupload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from s3files.views import FilePolicyAPI
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', TemplateView.as_view(template_name='upload.html'), name='upload-home'),
    path('api/files/policy/', FilePolicyAPI.as_view(), name='upload-policy'),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^form/', include('s3files.urls')),
]

#     ...
#     url(r'^upload/$', TemplateView.as_view(template_name='upload.html'), name='upload-home'),
#     url(r'^api/files/policy/$', FilePolicyAPI.as_view(), name='upload-policy'),
#     ...
# ]