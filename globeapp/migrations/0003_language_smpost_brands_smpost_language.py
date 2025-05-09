# Generated by Django 5.0.6 on 2025-04-03 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globeapp', '0002_alter_brands_id_alter_smpost_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='smpost',
            name='brands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='globeapp.brands'),
        ),
        migrations.AddField(
            model_name='smpost',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language', to='globeapp.language'),
        ),
    ]
