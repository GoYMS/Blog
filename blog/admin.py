from django.contrib import admin
from blog.models import TagModel, CategoryModel, EntryModel
# Register your models here.


class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'visiting', 'created_time', 'modifies_time']


admin.site.register(TagModel)
admin.site.register(CategoryModel)
admin.site.register(EntryModel)