from django.db import models
from taskapp.models import User


""" プロジェクトモデル """
class Project(models.Model):
    project_cd = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=25,
        verbose_name='プロジェクト名'
    )

    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leader',
        verbose_name='プロジェクトリーダ'
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='開始日'
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='終了日'
    )

    details = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='詳細'
    )

    update_date = models.DateField(
        auto_now=True
    )

    is_delete = models.BooleanField(
        default=False
    )
    
""" プロジェクト To ユーザ （1 対 多） """
class ProjectToUsers(models.Model):
    project_cd = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    user_cd = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

