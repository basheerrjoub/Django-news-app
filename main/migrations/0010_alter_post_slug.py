# Generated by Django 4.1.2 on 2022-10-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_post_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, null=True, unique_for_date="date"),
        ),
    ]
