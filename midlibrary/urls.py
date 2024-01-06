from django.contrib import admin
from django.urls import path
from mysite import views as mv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name="homepage"),
    path('book/<slug:slug>', mv.showpost, name="showpost"),
    path('book/<slug:slug>/borrow/', mv.borrow_book, name="borrow_book"),
    path('register/', mv.register),
    path('login/', mv.login, name='login'),
    path('logout/', mv.user_logout, name='logout'),
    path('search/', mv.search_books, name='search_books'),
    #path('book/<slug:slug>/return/', mv.return_book, name="return_book"),
]
