# Generated by Django 3.0.4 on 2020-12-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widget', '0002_widget_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='price',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
