# Generated by Django 3.2.9 on 2022-01-14 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Already',
            fields=[
                ('project_cd', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=25, null=True, verbose_name='課題名')),
            ],
        ),
        migrations.RemoveField(
            model_name='follow',
            name='id',
        ),
        migrations.AlterField(
            model_name='follow',
            name='subject_cd',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
