# Generated by Django 5.0 on 2023-12-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_created_post_updated_alter_post_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default='پیش نویس', max_length=15),
        ),
    ]