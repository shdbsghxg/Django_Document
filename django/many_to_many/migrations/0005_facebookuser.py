# Generated by Django 2.0.2 on 2018-02-06 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0004_auto_20180205_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friends', models.ManyToManyField(related_name='_facebookuser_friends_+', to='many_to_many.FacebookUser')),
            ],
        ),
    ]
