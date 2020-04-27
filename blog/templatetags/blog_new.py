from django import template
from blog.models import EntryModel, CategoryModel, TagModel

register = template.Library()


@register.simple_tag
def get_new_entries(num=5):
    """最新博客"""
    return EntryModel.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_popular_entries(num=5):
    """推荐博客"""
    return EntryModel.objects.all().order_by('-visiting')[:num]


@register.simple_tag
def get_category_entries():
    """分类"""
    return CategoryModel.objects.all()


@register.simple_tag
def get_tags():
    """标签"""
    return TagModel.objects.all()

