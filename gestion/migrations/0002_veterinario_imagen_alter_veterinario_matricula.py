# Generated by Django 5.1.3 on 2024-12-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterinario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='veterinarios/'),
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='matricula',
            field=models.CharField(max_length=50),
        ),
    ]