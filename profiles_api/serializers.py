from rest_framework import serializers

class HelloSearilizer(serializers.Serializer):
    """Serializes a name field for testing our api view"""
    name = serializers.CharField(max_length=10)
    