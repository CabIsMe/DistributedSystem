# Generated by Django 4.0.8 on 2022-11-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_id', models.IntegerField()),
                ('plan_title', models.TextField()),
                ('plan_content', models.TextField()),
                ('plan_desc', models.TextField()),
                ('plan_time', models.TextField()),
            ],
        ),
    ]
