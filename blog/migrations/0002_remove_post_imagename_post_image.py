# Generated by Django 4.1.1 on 2022-11-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="imageName",),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="posts"),
        ),
    ]
