from django.urls import path
from .views import *

urlpatterns = [
    path('', MembersList.as_view()),
]