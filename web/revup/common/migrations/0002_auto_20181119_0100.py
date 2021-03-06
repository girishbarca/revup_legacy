# Generated by Django 2.1.3 on 2018-11-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revup_common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'In Queue'), (1, 'Processing'), (2, 'Complete'), (-1, 'Error')], default=0),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]
