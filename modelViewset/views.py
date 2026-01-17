# it is ModelViewSet class inherits from GenericAPTView and includes implementation for various actions, by mixing in the behaviour of the various  mixin classes


from .models import Student
from .serializers import StudentsSerializer
from rest_framework import viewsets


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentsSerializer

class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentsSerializer