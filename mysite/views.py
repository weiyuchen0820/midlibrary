from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from mysite.models import Book, BorrowRecord
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegisterForm, LoginForm, BorrowForm, BookSearchForm, BookForm

# 主畫面
def homepage(request):
    posts = Book.objects.all()
    now = datetime.now()

    #抓使用者名稱
    user_name = None
    if request.user.is_authenticated:
        user_name = request.user.username

    return render (request, 'index.html', locals())

#書本的頁面
def showpost(request,slug):
    post = Book.objects.get(slug=slug)
    return render(request, 'post.html', {'post': post, 'book': post})

#辨識是否為superuser
def is_superuser(user):
    return user.is_superuser

#註冊
def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = User.objects.create_user(user_name, user_email, user_password)
                message = f'註冊成功！'
            else:
                message = f'兩次密碼不一致！'    
        return render(request, 'register.html', locals())
    else:
        message = "ERROR"
        return render(request, 'register.html', locals())
    
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import logout

#登入
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    message = '成功登入了'
                    user_name = user_name
                    return render(request, 'login.html', locals())
                else:
                    message = '帳號尚未啟用'
            else:
                message = '登入失敗'
                #user_name = '未登入'

        return render(request, 'login.html', locals())
    else:
        message = "ERROR"
        return render(request, 'login.html', locals())
 
#登出
def user_logout(request):
    logout(request)
    # 重定向到登录页面或任何其他页面
    return redirect('/')

#借還書系統
def rent_book(request):
    books = Book.objects.all()
    return render(request, 'rent_book.html', {'books': books})

#借書
@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    book.status = '可借閱'
    book.save()
    return redirect('rent_book')

'''
    if not book.status:
        book.status = 'borrowed'
        book.save()

    return HttpResponseRedirect(reverse('rent_book'))
'''


#還書
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    book = get_object_or_404(Book, pk=book_id)
    book.status = '外借中'
    book.save()
    return redirect('rent_book')

'''
    if book.status:
        book.status = 'available'
        book.save()

    return HttpResponseRedirect(reverse('rent_book'))
'''

#搜尋
@login_required
def search_books(request):
    form = BookSearchForm(request.GET)
    books = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        books = Book.objects.filter(title__icontains=search_query)

    return render(request, 'search.html', {'form': form, 'books': books})

@login_required
@user_passes_test(is_superuser)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

#新增書籍
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

#編輯書籍資料
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

#刪除書籍
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})

