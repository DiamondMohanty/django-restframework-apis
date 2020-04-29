from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TODO
from .serializers import TODOSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def todo(request):

    if request.method == 'GET':
        query_set = TODO.objects.all()
        serializer = TODOSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TODOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo_detail(request, id):

    try:
        todo = TODO.objects.get(pk=id)
    except TODO.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TODOSerializer(todo)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TODOSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

