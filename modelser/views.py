from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import students
from .serializers import StudentSerializer
from rest_framework import status
from django.http import Http404


class StudentApiView(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk is not None:
                stu = students.objects.get(id=pk)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            else:
                stu = students.objects.all()
                serializer = StudentSerializer(stu, many=True)
                return Response(serializer.data)
        except students.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None,format=None):
        try:
            stu = students.objects.get(id=pk)
        except students.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        try:
            stu = students.objects.get(id=pk)
        except students.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None, format=None):
        try:
            stu = students.objects.get(id=pk)
            stu.delete()
            return Response({"message": "Student deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except students.DoesNotExist:
            return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)