from django.contrib import admin
from mysite.models import book
# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display = ('title','slug','chap','author','body','pub_date')
admin.site.register(book, bookAdmin)