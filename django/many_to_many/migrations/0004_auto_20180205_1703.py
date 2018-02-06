# Generated by Django 2.0.2 on 2018-02-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0003_post_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', through='many_to_many.PostLike', to='many_to_many.User'),
        ),
    ]
