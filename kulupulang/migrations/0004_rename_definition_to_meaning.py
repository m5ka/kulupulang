from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kulupulang', '0003_auto_20220207_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='gloss',
            new_name='definition'
        ),
        migrations.AlterField(
            model_name='word',
            name='definition',
            field=models.TextField(help_text='what does this word mean? this will appear in the overall dictionary '
                                             'page with the part of speech.'),
        ),
        migrations.AlterField(
            model_name='word',
            name='etymology',
            field=models.TextField(blank=True, help_text="optionally, where does this word come from? this will only "
                                                         "appear on the word's page."),
        ),
        migrations.AlterField(
            model_name='word',
            name='notes',
            field=models.TextField(blank=True, help_text="any other optional notes about this word. this will only "
                                                         "appear on the word's page."),
        ),
    ]
