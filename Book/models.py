from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    # 元信息类
    class Meta:
        # 自定义表的名字
        db_table = 'bookinfo'


class PeopleInfo(models.Model):
    name = models.CharField(max_length=20)  # 人物姓名
    gender = models.BooleanField(default=True)  # 人物性别
    description = models.CharField(max_length=20)  # 人物描述
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'heroinfo'