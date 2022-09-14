from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from django.contrib import messages
from .forms import SettingForm
from .models import Setting


@staff_member_required
def settings_view(request):
    obj, _ = Setting.objects.get_or_create(
        site=request.site,
        defaults={
            'site_name': 'Demo'
        }
    )
    if request.method == 'POST':
        form = SettingForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'changed successfully.')
            return redirect(request.path)
    else:
        form = SettingForm(instance=obj)

    context = admin.site.each_context(request)
    context.update({
        'title': 'Base Info',
        'form':form
    })
    return render(request, 'settings/setting_form.html', context)
