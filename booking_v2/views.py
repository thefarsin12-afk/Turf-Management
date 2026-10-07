from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from booking_v2.serializer import SignUpSerializer,TurfBookingSerializer
from booking_v2.models import Booking

from datetime import time,datetime,timedelta

class SignUpRegisterView(APIView):

    def post (self,request):

        form_data = request.data

        serializer_instant = SignUpSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleaned_data = serializer_instant.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_instant = SignUpSerializer(user_object)

            return Response(data=serializer_instant.data)

        else:return Response(data=serializer_instant.errors)

class TurfBookingListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.AllowAny]

    def get(self,request):

        qs = Booking.objects.all()

        serializer_instant = TurfBookingSerializer(qs,many=True)

        return Response(data=serializer_instant.data)


    def post(self, request):

        form_data = request.data

        serializer_instant = TurfBookingSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleaned_data = serializer_instant.validated_data

            turf_id = cleaned_data.get("turf")

            booking_date = cleaned_data.get("booking_date")

            booking_time_details = time(7, 0)

            last_booking_object = Booking.objects.filter(turf=turf_id,booking_date=booking_date).last()

            if last_booking_object:

                next_booking_time = (datetime.combine(booking_date,last_booking_object.booking_time)+ timedelta(hours=2))

                booking_time_details = next_booking_time.time()

            qs = Booking.objects.create(**cleaned_data,booking_time=booking_time_details)

            serializer_instant = TurfBookingSerializer(qs)

            return Response(data=serializer_instant.data)

        else:

            return Response(data=serializer_instant.errors)
            