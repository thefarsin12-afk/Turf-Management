from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from turf_team_register.models import TurfRegister

from turf_team_register.serializer import TurfRegisterSerializer
# Create your views here.

class TurfRegisterListCreate(APIView):

    def get(self,request):

        qs = TurfRegister.objects.all()

        serializer_instants = TurfRegisterSerializer(qs,many=True)

        return Response(data=serializer_instants.data)