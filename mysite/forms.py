from django import forms

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(label='您的帳號', max_length=50)
    user_email = forms.EmailField(label='電子郵件')
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)
    user_password_confirm = forms.CharField(label='輸入確認密碼', widget=forms.PasswordInput)

class LoginForm(forms.Form):
    user_name = forms.CharField(label='您的帳號', max_length=50)
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)

class BorrowForm(forms.Form):
    borrower_name = forms.CharField(label='Your Name', max_length=100)
    return_date = forms.DateField(label='Return Date')

class BookSearchForm(forms.Form):
    search_query = forms.CharField(label='搜尋書籍', max_length=100)
