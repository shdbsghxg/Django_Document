# Generated by Django 2.0.2 on 2018-02-19 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_piece', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multiple_inheritance.Piece')),
            ],
            bases=('multiple_inheritance.piece',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_piece', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multiple_inheritance.Piece')),
            ],
            bases=('multiple_inheritance.piece',),
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multiple_inheritance.Article')),
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multiple_inheritance.Book')),
            ],
            bases=('multiple_inheritance.book', 'multiple_inheritance.article'),
        ),
    ]
