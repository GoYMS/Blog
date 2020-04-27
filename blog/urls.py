
from django.urls import re_path
from blog import views

urlpatterns = [
    # 首页
    re_path(r'^$', views.FirstView.as_view(), name='first'),
    # 主页
    re_path(r'^(?P<page_id>\d+)$', views.IndexView.as_view(), name='index'),
    # 详细页面
    re_path(r'^detail/(?P<blog_id>\d+)$', views.DetailView.as_view(), name='detail'),
    # 分类
    re_path(r'^category/(?P<cate_id>\d+)/(?P<page_id>\d+)$', views.CategoryView.as_view(), name='category'),
    # 标签
    re_path(r'^tag/(?P<tag_id>\d+)/(?P<page_id>\d+)$', views.TagView.as_view(), name='tag'),
    # 搜索
    re_path(r'^search/(?P<page_id>\d+)/$', views.SearchView.as_view(), name='search'),
    # 退出
    re_path(r'^logout/$', views.LogoutView.as_view(), name='logout'),

]
