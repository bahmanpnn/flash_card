from django.urls import path
from .views import *
urlpatterns = [
    path('',ListFlashCardAll.as_view(),name='all-flash-card-list'),
    path('create/',CreateFlashCard.as_view(),name='create-flash-card'),
    path('update/<id>/',UpdateFlashCard.as_view(),name='update-flash-card'),
    path('delete/<id>/',DeleteFlashCard.as_view(),name='delete-flash-card'),
    path('flash_card_list/<user_id>/',ListFlashCard.as_view(),name='user-flash-card-list'),
]