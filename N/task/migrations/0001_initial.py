from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('subject_cd', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='科目名')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_cd', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, verbose_name='課題名')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='開始日')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='期限')),
                ('now_date', models.DateField(blank=True, null=True, verbose_name='今の日付')),
                ('details', models.CharField(blank=True, max_length=200, null=True, verbose_name='詳細')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('kamoku', models.CharField(blank=True, max_length=200, null=True, verbose_name='科目名')),
                ('update_date', models.DateField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL, verbose_name='講師')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_cd', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='科目名')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_cd', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100, verbose_name='タスク名')),
                ('user_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='担当者名')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='開始日')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='期限')),
                ('details', models.CharField(blank=True, max_length=200, null=True, verbose_name='詳細')),
                ('priolity', models.IntegerField(choices=[(0, '未選択'), (1, '最低'), (2, '低'), (3, '普通'), (4, '高'), (5, '最高')], default=0)),
                ('update_date', models.DateField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='担当者')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectToUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project')),
                ('user_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectToTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project')),
                ('task_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='科目名')),
                ('subject_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.subject')),
            ],
        ),
    ]
