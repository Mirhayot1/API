from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookAPIView, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, BookListCreateApiView, BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')




urlpatterns = [
    # path('books/', BookAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/create/', BookListCreateApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls