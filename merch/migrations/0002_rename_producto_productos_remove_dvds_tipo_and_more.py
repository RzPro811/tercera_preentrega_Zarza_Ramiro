# Generated by Django 5.0.6 on 2024-07-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producto',
            new_name='Productos',
        ),
        migrations.RemoveField(
            model_name='dvds',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='dvds',
            name='precio',
            field=models.FloatField(),
        ),
    ]
