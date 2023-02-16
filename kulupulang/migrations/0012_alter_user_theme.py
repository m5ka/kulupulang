# Generated by Django 3.2.17 on 2023-02-06 21:56

from django.db import migrations, models
import django.db.models.deletion


def convert_theme(apps, schema_editor):
    User = apps.get_model("kulupulang", "User")
    Theme = apps.get_model("kulupulang", "Theme")
    for user in User.objects.all():
        if user.theme:
            try:
                user.theme = Theme.objects.get(name=user.theme).id
                user.save()
            except Theme.DoesNotExist:
                user.theme = 1
                user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("kulupulang", "0011_theme"),
    ]

    operations = [
        migrations.RunPython(convert_theme, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name="user",
            name="theme",
            field=models.ForeignKey(
                default=1,
                help_text="the theme you want to display the site in",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="kulupulang.theme",
            ),
        ),
    ]
