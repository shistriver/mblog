# Generated by Django 2.1.4 on 2018-12-23 18:02

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]