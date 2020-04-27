from django.shortcuts import render, redirect, reverse
from django.views.generic import View
import markdown
import pygments
from django.db.models import Q
from django.contrib.auth import logout


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import EntryModel, CategoryModel, TagModel

# Create your views here.


class FirstView(View):
    """跳转到首页"""
    def get(self, request):
        return redirect(reverse('blog:index', kwargs={'page_id': 1}))


class IndexView(View):
    """首页"""
    def get(self, request, page_id):
        entries = EntryModel.objects.all()
        paginator = Paginator(entries, 2)
        try:
            page_entry = paginator.page(page_id)
        except PageNotAnInteger:
            page_entry = paginator.page(1)
        except EmptyPage:
            page_entry = paginator.page(1)

        return render(request, 'index.html', locals())


class DetailView(View):
    """详情页"""
    def get(self, request, blog_id):
        entry = EntryModel.objects.get(id=blog_id)
        # 访问量加1
        entry.visiting += 1
        entry.save()

        # 将正文内容显示为markdown格式
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 设置文章的目录格式
            'markdown.extensions.toc'
        ])
        entry.body = md.convert(entry.body)
        # 显示文章的目录格式
        entry.toc = md.toc

        return render(request, 'detail.html', locals())


class CategoryView(View):
    """分类"""
    def get(self, request, cate_id, page_id):
        c = CategoryModel.objects.get(id=cate_id)
        entries = EntryModel.objects.filter(category=c)
        paginator = Paginator(entries, 1)
        try:
            page_entry = paginator.page(page_id)
        except PageNotAnInteger:
            page_entry = paginator.page(1)
        except EmptyPage:
            page_entry = paginator.page(1)

        return render(request, 'category.html', locals())


class TagView(View):
    """标签"""
    def get(self, request, tag_id, page_id):
        t = TagModel.objects.get(id=tag_id)
        entries = EntryModel.objects.filter(tags=t)
        paginator = Paginator(entries, 1)
        try:
            page_entry = paginator.page(page_id)
        except PageNotAnInteger:
            page_entry = paginator.page(1)
        except EmptyPage:
            page_entry = paginator.page(1)

        return render(request, 'tags.html', locals())


class SearchView(View):
    """搜索"""
    def get(self, request, page_id):
        search = request.GET.get('search', '')
        if search == '':
            # 为空
            return redirect(reverse('blog:index'))
        entries = EntryModel.objects.filter(Q(title__icontains=search) |
                                  Q(body__icontains=search) |
                                  Q(abstract__icontains=search))

        paginator = Paginator(entries, 1)
        try:
            page_entry = paginator.page(page_id)
        except PageNotAnInteger:
            page_entry = paginator.page(1)
        except EmptyPage:
            page_entry = paginator.page(1)

        return render(request, 'search.html', locals())


class LogoutView(View):
    """用户退出"""

    def get(self, request):
        logout(request)
        return redirect(reverse('blog:index', kwargs={'page_id':1}))







