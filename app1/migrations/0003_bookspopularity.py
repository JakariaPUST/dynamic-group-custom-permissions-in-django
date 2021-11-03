# Generated by Django 3.2.9 on 2021-11-02 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_books_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksPopularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.IntegerField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.books')),
            ],
        ),
    ]