from datetime import datetime, timedelta
from library.models import Book, User
import pytz
def fine_calc(book):
    days = (book.issue_time-datetime.now()).days
    return days

def issue(book_id,user_id):
    book = Book.objects.get(book_id=book_id)
    user = User.objects.get(user_id=user_id)
    book.issued_to = user
    book.status = 'Issued'
    book.issue_time = datetime.now()
    book.save()
    user.borrowed_book = book
    user.save()
    return "Book issued successfully"

def return_func(request,pk):
    book_id = pk
    book = Book.objects.get(book_id=book_id)
    if book.status == "Available":
        return "Book Already Available"
    timezone = pytz.timezone('UTC')
    date_now = datetime.now(timezone)
    issued_time = book.issue_time
    date_diff = (date_now-issued_time)
    date_diff = date_diff.days
    if date_diff > 7 and not request.data.get('fine'):
        return f"Please Pay the Fine {(date_diff-7)*10}"
    user = book.issued_to
    book.issued_to = None
    book.status = 'Available'
    book.issue_time = None
    book.save()
    user.borrowed_book = None
    user.save()
    return "Book returned successfully"