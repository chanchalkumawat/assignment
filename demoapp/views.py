from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserList(APIView):

    def get(self, request, format=None):

        if self.request.query_params.get('userid'):
            try:
                user = User.objects.get(user_id=self.request.query_params.get('userid'))
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return HttpResponse(status=404)

        elif self.request.query_params.get('date'):
            user = User.objects.filter(date=self.request.query_params.get('date'))
            if len(user) != 0:
                serializer = UserSerializer(user, many=True)
                return Response(serializer.data)
            else:
                return HttpResponse(status=404)

        elif self.request.query_params.get('city'):
            user = User.objects.filter(city__iexact=self.request.query_params.get('city'))
            if len(user) != 0:
                serializer = UserSerializer(user, many=True)
                return Response(serializer.data)
            else:
                return HttpResponse(status=404)

        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
