# Generated by Django 5.0 on 2024-02-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_register_alter_admin_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tourcode', models.CharField(max_length=10)),
                ('tourname', models.CharField(max_length=30)),
                ('tourpackage', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'package_table',
            },
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='phno',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
