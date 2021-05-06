from django.contrib import admin

from news.models import Article, Author

# Register your models here.

admin.site.register(Article)
admin.site.register(Author)