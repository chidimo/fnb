# Generated by Django 3.2 on 2021-04-19 14:53

from django.db import migrations, models
import django.utils.timezone
import utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('points', models.IntegerField(default=5)),
            ],
            options={
                'ordering': ['points'],
            },
        ),
    ]