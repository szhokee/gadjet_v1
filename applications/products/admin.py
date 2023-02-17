from django.contrib import admin
from applications.products.models import *


class ImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ('image',)
    max_num = 4


# class ProductAdmin(admin.ModelAdmin):
#     inlines = (ImageAdmin,)

#     list_display = ('title', 'owner', 'post_count', 'created_at', 'john',)
#     list_filter = ('owner',)
#     search_fields = ('title',)
#     exclude = ('john',)                                           #скрывает название поста в админ панеле

#     def post_count(self, obj):
#         return obj.likes.filter(is_like=True).count()


admin.site.register(Product)
admin.site.register(ProductImage)