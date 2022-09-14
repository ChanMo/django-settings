# Generated by Django 4.1.1 on 2022-09-14 02:33

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0002_setting_signup_enabled"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="setting",
            name="signup_enabled",
        ),
        migrations.AddField(
            model_name="setting",
            name="admin_login_bg",
            field=sorl.thumbnail.fields.ImageField(
                blank=True,
                null=True,
                upload_to="uploads/",
                verbose_name="the image of login page",
            ),
        ),
        migrations.AddField(
            model_name="setting",
            name="copyright",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="setting",
            name="logo",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, null=True, upload_to="uploads/"
            ),
        ),
        migrations.AlterField(
            model_name="setting",
            name="site_name",
            field=models.CharField(max_length=200),
        ),
    ]
