# Generated by Django 2.0.5 on 2018-05-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0003_auto_20180526_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='artcilesource',
            name='cached_properties',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]