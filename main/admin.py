from django.contrib import admin
from .models import Post, Author

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("author", "date")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
