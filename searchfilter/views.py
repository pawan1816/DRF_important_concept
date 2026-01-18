# from django.shortcuts import render
# from .serializers import StudentSerializer
# from rest_framework.generics import ListAPIView
# from .models import Student
# from rest_framework.filters import SearchFilter

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends=[SearchFilter]

#     # exact matech
#     # search_fields=['=name']

#     # start with
#     search_fields=['^name','^city']






# --------------------------------------


# orderering filter


# --------------------------------------------




from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[OrderingFilter]
    # ordering_fields=['city']
    ordering_fields=['city','name']