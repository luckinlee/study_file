from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 用户表,扩展与auth表的结构
class UserInfo(AbstractUser):
    phone = models.IntegerField(null=True)
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.png')
    blog = models.OneToOneField(to='Blog', null=True)  # 关联个人站点
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# 个人站点表
class Blog(models.Model):
    site_name = models.CharField(max_length=32, verbose_name='站点名称')
    site_title = models.CharField(max_length=32, verbose_name='站点标题')
    site_theme = models.CharField(max_length=64, verbose_name='站点样式')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='文章分类')
    blog = models.ForeignKey(to='Blog', null=True)  # 关联个人站点
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='文章标签')
    blog = models.ForeignKey(to='Blog', null=True)  # 关联个人站点
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章简介')
    content = models.TextField(verbose_name="文章内容")
    up_num = models.BigIntegerField(default=100)
    down_num = models.BigIntegerField(default=100)
    comment_num = models.BigIntegerField(default=100, verbose_name='评论数')
    blog = models.ForeignKey(to='Blog', null=True)  # 关联个人站点
    category = models.ForeignKey(to='Category', null=True)
    tags = models.ManyToManyField(to='Tag', through='ArticleTag', through_fields=('article', 'tag'))
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# 文章关联标签中间表
class ArticleTag(models.Model):
    article = models.ForeignKey(to='Article')
    tag = models.ForeignKey(to='Tag')


# 点赞表
class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    is_up = models.BooleanField(verbose_name='是否点赞')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


# 评论表
class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article')
    content = models.CharField(max_length=255)
    parent = models.ForeignKey(to='self', null=True)  # 跟评论或者子评论
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
