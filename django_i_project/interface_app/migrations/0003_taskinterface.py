# Generated by Django 2.1 on 2020-05-24 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0002_interface'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(db_index=True, default=0, verbose_name='任务id')),
                ('interface_id', models.IntegerField(default=0, verbose_name='接口id')),
            ],
        ),
    ]
