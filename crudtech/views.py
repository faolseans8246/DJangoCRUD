from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import MyBase
from .serializer import MySerializer

# Create your views here.


# to'planuvhci qismi bilan ishlash qismi
@api_view(["GET", "POST"])
def contain(request):
    if request.method == 'GET':
        cruds = MyBase.objects.all()
        serializer = MySerializer(cruds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ID bilan bitta elament orqali ishlash qismi
@api_view(["GET", "PUT", "DELETE"])
def only(request, pk):

    try:
        cruds = MyBase.objects.get(pk=pk)
    except MyBase.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


    if request.method == "GET":
        serializer = MySerializer(cruds)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MySerializer(cruds, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        cruds.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)