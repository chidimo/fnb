# Generated by Django 3.2 on 2021-04-21 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_alter_person_options'),
        ('voting', '0004_rename_vote_vote_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='voter', to='people.person'),
            preserve_default=False,
        ),
    ]