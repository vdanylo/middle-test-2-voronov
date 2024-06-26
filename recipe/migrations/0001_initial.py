# Generated by Django 4.2.1 on 2023-05-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('cover_image', models.ImageField(upload_to='book_covers/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('authors', models.ManyToManyField(to='recipe.author')),
            ],
        ),
    ]
