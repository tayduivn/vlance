# Generated by Django 2.2.2 on 2019-06-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='file',
            field=models.FileField(default='', null=True, upload_to='', verbose_name='File đính kèm'),
        ),
    ]
