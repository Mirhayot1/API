from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from .serializers import BookSerializer
# Create your views here.

# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }
        return Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                'status': 'Succesfull',
                'book':serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                    {'status':'Does not exits',
                 'message':"Book is not found"},
                status=status.HTTP_404_NOT_FOUND
            )

# class BookDeleteApiView(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status':True,
                'message':"Successfully deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': False,
                'Message': "Book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)





class BookUpdateApiView(APIView):

    def put(self, request, pk):
        from django.shortcuts import get_object_or_404
        book = get_object_or_404(Book.object.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                'status':True,
                'message': f"Book {book_saved} updated successfully"

            }
        )






class BookListCreateApiView(APIView):

    def post(self, request, pk):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': f"book save database",
                'books': data
            }
        return Response(data)


# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# @api_view(['GET'])
# def book_list_view(request, *args, *kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)