# Generated by Django 5.1.3 on 2024-12-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_veterinario_imagen_alter_veterinario_matricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veterinario',
            old_name='imagen',
            new_name='foto',
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]