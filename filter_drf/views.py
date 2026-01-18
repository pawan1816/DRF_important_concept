from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

# without filter
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class=StudentSerializer


# with filter django filter based on attributes senerio 1

# class StudentList(ListAPIView):
#     queryset = Student.objects.filter(passby='user1')
#     serializer_class=StudentSerializer




# -------------------------------------------------------------------------

# # with authentication filter (based on current user like which is login on )

# from rest_framework.permissions import IsAuthenticated

# class StudentList(ListAPIView):
#     serializer_class = StudentSerializer

#     def get_queryset(self):
#         return Student.objects.filter(passby=self.request.user)



# -----------------------------------------------

# Generic Filtering with drf



# use djangofilterBackend


# to use this we need to install 

# pip install django-filter
# and add django_filters

# this type of url we have to type 

# http://127.0.0.1:8000/studentapi/?passby=user1
# -----------------------------------------------


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['passby','name']