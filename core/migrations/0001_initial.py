# Generated by Django 2.0 on 2017-12-09 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_title', models.CharField(max_length=200)),
                ('mission_desecription', models.CharField(max_length=10000)),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case_title', models.CharField(max_length=200)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mission')),
            ],
        ),
    ]