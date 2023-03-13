# Generated by Django 4.0.6 on 2022-07-31 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
