# Generated by Django 3.2.25 on 2024-03-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
