from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    image = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    chap = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)
    body = models.TextField(null=False, blank=True)
    pub_date = models.DateField()
    status = models.BooleanField(("外借中"), default=False)

    @property
    def formatted_status(self):
        if self.status:
            return '<span style="color: black; border: 1px solid green;padding: 3px; border-radius: 8px;">可借閱</span>'
        else:
            return '<span style="color: black; border: 1px solid red; padding: 3px; border-radius: 8px;">外借中</span>'

    formatted_status.fget.short_description = "外借狀態"

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self) -> str:
        return self.title
    
    @property
    def display_status(self):
        return dict(self.STATUS_CHOICES)[self.status]

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} borrowed {self.book.title} on {self.borrow_date}"
    