from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    chap = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField(null=False,blank=True)
    pub_date = models.DateField()

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self) -> str:
        return self.title