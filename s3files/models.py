from django.db import models
from django.conf import settings
# Create your models here.
from django.db import models
from s3direct.fields import S3DirectField


class Cat(models.Model):
    custom_filename = S3DirectField(dest='custom_filename', blank=True)


class Kitten(models.Model):
    mother = models.ForeignKey('Cat', on_delete=models.CASCADE)

    video = S3DirectField(dest='videos', blank=True)
    image = S3DirectField(dest='images', blank=True)
    pdf = S3DirectField(dest='pdfs', blank=True)


class FileItem(models.Model):
    user                            = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    name                            = models.CharField(max_length=120, null=True, blank=True)
    path                            = models.TextField(blank=True, null=True)
    size                            = models.BigIntegerField(default=0)
    file_type                       = models.CharField(max_length=120, null=True, blank=True)
    timestamp                       = models.DateTimeField(auto_now_add=True)
    updated                         = models.DateTimeField(auto_now=True)
    uploaded                        = models.BooleanField(default=False)
    active                          = models.BooleanField(default=True)

    @property
    def title(self):
        return str(self.name)
