from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserModel(AbstractUser, models.Model):
    """用户模型类"""

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class CategoryModel(models.Model):

    name = models.CharField(max_length=128, verbose_name='博客分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'


class TagModel(models.Model):

    name = models.CharField(max_length=128, verbose_name='博客标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = '博客标签'


class EntryModel(models.Model):

    title = models.CharField(max_length=128, verbose_name='文章标题')

    author = models.ForeignKey('UserModel', on_delete=models.CASCADE, verbose_name='博客作者')

    image = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='博客图片')

    body = models.TextField(verbose_name='博客正文')

    abstract = models.TextField(max_length=256, blank=True, null=True, verbose_name='博客摘要')

    visiting = models.PositiveIntegerField(default=0, verbose_name='博客访问量')

    category = models.ManyToManyField('CategoryModel', verbose_name='博客分类')

    tags = models.ManyToManyField('TagModel', verbose_name='博客标签')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    modifies_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客'
        verbose_name_plural = '博客'














