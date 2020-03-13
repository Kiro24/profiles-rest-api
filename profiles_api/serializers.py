from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Acts as django forms to handle validation of python/JSON data accross api"""
    name = serializers.CharField(max_length=10)