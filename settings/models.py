from django.db import models
from django.contrib.sites.models import Site
from sorl.thumbnail import ImageField


class Setting(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=200)
    logo = ImageField(blank=True, null=True, upload_to='uploads/')
    admin_login_bg = ImageField('the image of login page', blank=True, null=True, upload_to='uploads/')
    copyright = models.CharField(max_length=200, blank=True, null=True)
