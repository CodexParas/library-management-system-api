from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=(('Available','Available'),('Issued','Issued')),default='Available')
    issued_to = models.ForeignKey("library.user", on_delete=models.CASCADE, blank=True, null=True)
    added = models.DateTimeField(auto_now=True)
    issue_time = models.DateTimeField(blank=True,null=True)

    def issue(self,user):
        self.status = 'Issued'
        self.issued_to = user
        self.issue_time = datetime.now()
    
    def return_book(self):
        self.status = 'Available'
    
    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    user_status = models.CharField(max_length=50,choices=(('Libraian','Libraian'),('Student','Student')),default='Student')
    borrowed_book = models.ForeignKey("library.Book", on_delete=models.CASCADE, blank=True, null=True)

    def borrow_book(self,book):
        book.issue(self)
        self.borrowed_book = book

    def return_book(self,book):
        book.return_book()
        self.borrowed_book = 0
    
    def __str__(self):
        return self.name
    