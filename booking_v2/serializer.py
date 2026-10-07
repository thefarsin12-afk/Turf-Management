from django.contrib.auth.models import User

from rest_framework import serializers

from booking_v2.models import Booking


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class TurfBookingSerializer(serializers.ModelSerializer):

    booking_time = serializers.TimeField(read_only=True)

    class Meta:
        
        model = Booking

        fields = '__all__'

        read_only_fields = ["id", "booking_time"]


        """ def validate(self,validate_data):

          end_time = validate_data.get("duration")

          if end_time >= time(21, 0):
               
                raise serializers.ValidationError("Turf Closed")

          return validate_data"""