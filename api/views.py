from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import MemberListSerializer

# Create your views here.


class MembersList(generics.ListAPIView):
    queryset = MembersList.objects.all()
    serializer_class = MemberListSerializer
