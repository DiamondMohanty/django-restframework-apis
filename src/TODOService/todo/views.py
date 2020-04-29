from .models import TODO
from .serializers import TODOSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TODOList(APIView):

    def get(self, request, format=None):
        query_set = TODO.objects.all()
        serializer = TODOSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = TODOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class TODODetails(APIView):

    @staticmethod
    def get_todo(pk):
        try:
            todo = TODO.objects.get(pk=pk)
            return todo
        except TODO.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        todo = TODODetails.get_todo(id)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TODOSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        todo = TODODetails.get_todo(id)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = JSONParser().parse(request)
        serializer = TODOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        todo = TODODetails.get_todo(id)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


