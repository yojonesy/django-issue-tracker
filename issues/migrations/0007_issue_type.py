# Generated by Django 3.2.5 on 2021-12-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_auto_20211230_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.IntegerField(choices=[(0, 'Bug'), (1, 'Feature')], default=0),
        ),
    ]
