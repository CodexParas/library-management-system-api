from django.shortcuts import render
from rest_framework import viewsets
from library.models import Book, User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from library.serializer import BookSerializer, UserSerializer
from datetime import datetime
from library.helpers import fine_calc, issue, return_func
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['post'], detail=True,
            url_path='issue', url_name='issue')
    def issue_book(self,request,pk=None):
        book_id = pk
        user_id = request.data.get('user_id')
        res = issue(book_id,user_id)
        return Response({'message': res})

    @action(methods=['post'], detail=True,
            url_path='return', url_name='return')
    def return_book(self,request,pk=None):
        res = return_func(request,pk)
        return Response({'message': res})


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer