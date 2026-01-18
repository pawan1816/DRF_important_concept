# ----------------------------------------------

# Page Number Pagination

# ---------------------------------------------


# from django.shortcuts import render
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView
# from .models import Student
# from rest_framework.filters import OrderingFilter

# # perview pagination
# # from rest_framework.pagination import PageNumberPagination
 
#  #custom pagination class
# from .mypagination import Mypagination

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends=[OrderingFilter]
#     ordering_fields=['id','name']
#     # pagination_class=PageNumberPagination
#     pagination_class= Mypagination




# --------------------------------------------------------

# Limit Offside Pagination

# from where and how many item in a page

# ---------------------------------------------------------




# from django.shortcuts import render
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView
# from .models import Student
# from rest_framework.filters import OrderingFilter

# # perview pagination
# # from rest_framework.pagination import LimitOffsetPagination
 
# #  #custom pagination class
# from .mypagination import Mypagination

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends=[OrderingFilter]
#     ordering_fields=['id','name']
#     pagination_class=Mypagination
#     # pagination_class= LimitOffsetPagination




# -----------------------------

# Cursor pagination it only allow previous and next

# -----------------------------


from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import OrderingFilter

 
#  #custom pagination class
from .mypagination import Mypagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['id','name']
    pagination_class=Mypagination