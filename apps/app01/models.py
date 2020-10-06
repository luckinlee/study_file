from django.db import models


# Create your models here.
class Userinfo(models.Model):
    username = models.CharField(unique=True, max_length=16, verbose_name='用户名')
    password = models.IntegerField(max_length=16, verbose_name='密码')

    def __str__(self):
        return self.username


class Author(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='姓名')
    age = models.CharField(max_length=32, verbose_name='年龄')
    # 作者详情表的一对一外键
    author_detail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    birthday = models.DateField()
    telephone = models.BigIntegerField(verbose_name='手机号')
    addr = models.CharField(max_length=64, verbose_name='地址')


class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社')
    city = models.CharField(max_length=32, verbose_name='出版社城市')


class Book(models.Model):
    book_name = models.CharField(max_length=32, verbose_name='书名')
    publish_data = models.DateField()
    price = models.IntegerField()
    # 关联出版社,一对多
    publish = models.ForeignKey(to='Publish', verbose_name='关联出版社id')
    # 作者和书籍关联关系,多对多
    author = models.ManyToManyField(to='Author', )
