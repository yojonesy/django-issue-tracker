# Generated by Django 3.2.8 on 2021-10-14 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='linked_issues',
            field=models.ManyToManyField(blank=True, to='issues.Issue'),
        ),
    ]
