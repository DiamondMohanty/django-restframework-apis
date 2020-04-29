from rest_framework import serializers
from .models import TODO


class TODOSerializer(serializers.ModelSerializer):
    '''
        Model Serializer provide the default implementation of the create and update method implementations.
    '''
    class Meta():
        model = TODO
        fields = ['id', 'description', 'completion_date', 'status']

