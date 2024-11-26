from django.urls import path
from .views import BookReservationView, user_profile_and_books


urlpatterns = [
    path('user/profile/', user_profile_and_books, name='user-profile'),
    path('reserve/<int:book_id>/', BookReservationView.as_view(), name='reserve_book_api'),
]
