from rest_framework import serializers
from library.models import Book, User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    book_id = serializers.ReadOnlyField()
    class Meta:
        model = Book
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = "__all__"