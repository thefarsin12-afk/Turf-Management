from rest_framework import serializers

class TurfRegisterSerializer(serializers.Serializer):

    team_name = serializers.CharField()

    phone_number = serializers.IntegerField()

    date = serializers.DateTimeField(read_only=True)

    duration = serializers.CharField(read_only=True)