from django.contrib import admin
from .models import Author, Book


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'author', 'description')
admin.site.register(Author)
admin.site.register(Book, MemberAdmin)