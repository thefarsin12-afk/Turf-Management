from rest_framework import serializers

class TurfSerializer(serializers.Serializer):

    id = serializers.CharField(read_only = True)
    
    name = serializers.CharField()

    location = serializers.CharField()

    email = serializers.EmailField()

    phone_number = serializers.IntegerField()


class UserSerializers(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()