# Generated by Django 3.2.25 on 2024-05-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'nebulo'), ('ESTRELA', 'estrela'), ('GALAXIA', 'galaxia'), ('PLANETA', 'planeta')], default='', max_length=100),
        ),
    ]
