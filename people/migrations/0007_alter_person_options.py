# Generated by Django 3.2 on 2021-04-21 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_delete_personvote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name_plural': 'persons'},
        ),
    ]
