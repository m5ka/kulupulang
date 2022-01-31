# Generated by Django 3.2.11 on 2022-01-31 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import kulupulang.models.base.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('kulupulang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(db_index=True, help_text="a nice little name for this batch you're cooking up. any name will do.", max_length=255)),
                ('description', models.TextField(blank=True, help_text="this is optional, but if you feel like giving a little description then hey that's totally cool")),
                ('submitted', models.BooleanField(default=False)),
                ('submitted_at', models.DateTimeField(null=True)),
                ('flagged', models.BooleanField(default=False)),
                ('passed', models.BooleanField(default=False)),
                ('passed_at', models.DateTimeField(null=True)),
                ('voting_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('voting_hours', models.IntegerField(default=48, help_text="how many hours should this stay in the oven before it's cooked and in the dictionary?")),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('root', models.CharField(db_index=True, help_text="this is the root itself. make sure it's valid as a root!", max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('gloss', models.TextField(help_text="what's the general meaning of this root?")),
                ('notes', models.TextField(blank=True, help_text='this is for any optional notes you may want to make about this root.')),
                ('passed', models.BooleanField(default=False)),
                ('passed_at', models.DateTimeField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kulupulang.batch')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, kulupulang.models.base.mixins.AutoSlugMixin),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('headword', models.CharField(db_index=True, help_text='this is the word itself.', max_length=255)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('pos', models.CharField(choices=[('noun', 'noun'), ('verb', 'verb'), ('particle', 'particle'), ('pronoun', 'pronoun')], max_length=128)),
                ('cls', models.CharField(blank=True, choices=[('akulu', 'animate kulupu'), ('ikulu', 'inanimate kulupu'), ('nkulu', 'non-kulupu')], max_length=128)),
                ('gloss', models.TextField(help_text='what does this word mean?')),
                ('etymology', models.TextField(blank=True, help_text='optionally, where does this word come from?')),
                ('notes', models.TextField(blank=True, help_text='any other optional notes about this word')),
                ('passed', models.BooleanField(default=False)),
                ('passed_at', models.DateTimeField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kulupulang.batch')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('roots', models.ManyToManyField(to='kulupulang.Root')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, kulupulang.models.base.mixins.AutoSlugMixin),
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('resolved', models.BooleanField(default=False)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kulupulang.batch')),
                ('opened_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
