# Generated by Django 4.0.3 on 2022-04-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagrams', '0003_alter_ai_one_current_alter_ai_one_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ai_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.DecimalField(decimal_places=6, max_digits=50, verbose_name='current')),
                ('sts', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='ai_one',
            name='sts',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], max_length=2),
        ),
    ]