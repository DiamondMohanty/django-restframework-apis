from .models import TODO
from .serializers import TODOSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class TODOList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    permission_classes = (IsAuthenticated, )

    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TODODetails(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


