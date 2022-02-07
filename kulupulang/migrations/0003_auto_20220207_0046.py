# Generated by Django 3.2.11 on 2022-02-07 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kulupulang', '0002_batch_discussion_root_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='roots',
        ),
        migrations.AlterField(
            model_name='word',
            name='pos',
            field=models.CharField(choices=[('noun', 'noun'), ('verb', 'verb'), ('particle', 'particle'), ('pronoun', 'pronoun'), ('adjective', 'adjective'), ('adverb', 'adverb'), ('determiner', 'determiner'), ('root', 'root'), ('affix', 'affix')], max_length=128),
        ),
        migrations.DeleteModel(
            name='Root',
        ),
    ]
