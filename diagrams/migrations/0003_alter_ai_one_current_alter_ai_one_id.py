# Generated by Django 4.0.3 on 2022-04-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagrams', '0002_alter_ai_one_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_one',
            name='current',
            field=models.DecimalField(decimal_places=6, max_digits=50, verbose_name='current'),
        ),
        migrations.AlterField(
            model_name='ai_one',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
