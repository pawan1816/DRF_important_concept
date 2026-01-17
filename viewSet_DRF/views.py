from .models import Student
from .serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        print("***************List*******************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Details",self.detail)
        print("Suffix", self.suffix)
        print("Name",self.name)
        print("Description",self.description)

        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("***************Retrive*******************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Details",self.detail)
        print("Suffix", self.suffix)
        print("Name",self.name)
        print("Description",self.description)

        student = get_object_or_404(Student, pk=pk)
        serializer = StudentsSerializer(student)
        return Response(serializer.data)

    def create(self, request):
        print("***************Create*******************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Details",self.detail)
        print("Suffix", self.suffix)
        print("Name",self.name)
        print("Description",self.description)

        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg': 'Data Created'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print("***************Update*******************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Details",self.detail)
        print("Suffix", self.suffix)
        print("Name",self.name)
        print("Description",self.description)

        student = get_object_or_404(Student, pk=pk)
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg': 'Complete data updated'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print("***************Partial Update*******************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Details",self.detail)
        print("Suffix", self.suffix)
        print("Name",self.name)
        print("Description",self.description)

        student = get_object_or_404(Student, pk=pk)
        serializer = StudentsSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg': 'Partial data updated'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        print("***************Destroy*******************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Details",self.detail)
        print("Suffix", self.suffix)
        print("Name",self.name)
        print("Description",self.description)
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(
            {'msg': 'Data Deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
