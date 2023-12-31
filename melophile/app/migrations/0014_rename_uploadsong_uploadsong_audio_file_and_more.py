# Generated by Django 4.2.5 on 2023-10-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_audiofile_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadsong',
            old_name='uploadsong',
            new_name='audio_file',
        ),
        migrations.AddField(
            model_name='uploadsong',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='uploadsong',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
