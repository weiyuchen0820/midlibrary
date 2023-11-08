from django.contrib import admin
from mysite.models import Book
# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ('image','title','slug','chap','author','body','pub_date')
admin.site.register(Book, bookAdmin)