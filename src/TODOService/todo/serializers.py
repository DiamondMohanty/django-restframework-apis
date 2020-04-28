from rest_framework import serializers
from .models import TODO


class TODOSerializer(serializers.Serializer):

    """
        TODOSerializer helps in serializing the python class objects into json format and vice versa
    """
    # It is preferable to keep the name of serializer class variables same as the Python class to be serialized.
    # These fields are serialized and deserialized.
    # The field flags determine how the serializer will be displayed under various circumstances
    # e.g like rendering to HTML.
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=255, required=True, allow_blank=False)
    completion_date = serializers.DateTimeField(required=False)
    status = serializers.BooleanField(required=False, default=False)

    def create(self, validated_data):
        # This method is called when a object is instantiated by serializer.save()
        return TODO.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # The instance is a class instance and validated_data is the new data which needs to be set the instance.
        # This method is called when a object is updated by serializer.save()
        instance.description = validated_data.get('description', instance.description)
        instance.completion_date = validated_data.get('completion_date', instance.completion_date)
        instance.status = validated_data.get('description', instance.status)
        instance.save()
        return instance

