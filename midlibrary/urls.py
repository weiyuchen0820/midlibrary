from django.contrib import admin
from django.urls import path
from mysite import views as mv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name="homepage"),
    path('book/<slug:slug>', mv.showpost, name="showpost"),
    #使用者管理相關
    path('register/', mv.register),
    path('login/', mv.login, name='login'),
    path('logout/', mv.user_logout, name='logout'),
    #搜尋
    path('search/', mv.search_books, name='search_books'),
    #書本管理相關
    path('book_list/', mv.book_list, name='book_list'),
    path('add_book/', mv.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', mv.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', mv.delete_book, name='delete_book'),
    #借還書相關
    path('rent_book/', mv.rent_book, name='rent_book'),
    path('borrow/<int:book_id>/', mv.borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', mv.return_book, name='return_book'),
]
