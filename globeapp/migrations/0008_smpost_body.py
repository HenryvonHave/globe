# Generated by Django 5.0.6 on 2025-04-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globeapp', '0007_smpost_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='smpost',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
