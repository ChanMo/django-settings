# 站点设置

为django提供后台可编辑的配置方案, 同时也方便request调用

## Quick Start

修改`settings.py`

```
INSTALLED_APPS = [
    ...
    'django.contrib.sites',    
    'settings',
    ...
]

SITE_ID = 1
```

更新数据库

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

在views中使用

```
def index(request):
    settings = request.site.setting
```

在templates中使用

```
<img src="{{request.site.setting.logo.url}}" alt="logo" />
```
