from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn', 'price',)

        # def validate(self, data):
        #     title = data.get('title', None)
        #     author = data.get('author', None)
        #
        #     if not title.isalpha():
        #         raise ValidationError(
        #             {
        #                 'status':False,
        #                 'message': "kitob sarlavhasi satr bo'lishi kerak!"
        #             }
        #         )
        #
        #     if Book.objects.filter(title=title, author=author).exists():
        #         raise ValidationError(
        #             {
        #                 'status': False,
        #                 'message': "Muallifva kitob sarlavhasi bir xil bo'lishi mumkin emas!"
        #             }
        #         )
        #
        #     return data