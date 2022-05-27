from django.db import models
from django.contrib.sites.models import Site
# from sorl.thumbnail import ImageField


class Setting(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    site_name = models.CharField('站点名称', max_length=200)
    # logo = ImageField('LOGO', blank=True, null=True)
    signup_enabled = models.BooleanField('是否开放注册', default=False)
