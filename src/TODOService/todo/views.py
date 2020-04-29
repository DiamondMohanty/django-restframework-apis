from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .models import TODO
from .serializers import TODOSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def todo(request, format=None):

    if request.method == 'GET':
        query_set = TODO.objects.all()
        serializer = TODOSerializer(query_set, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TODOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id, format=None):

    try:
        todo = TODO.objects.get(pk=id)
    except TODO.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TODOSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TODOSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

