
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
from .models import User

class UserList(APIView):

    def get(self, request, format=None):

        if self.request.query_params.get('userid'):
            user=User.objects.get(user_id=self.request.query_params.get('userid'))
            serializer = UserSerializer(user)
            return Response(serializer.data)

        elif self.request.query_params.get('date'):
            user = User.objects.filter(date=self.request.query_params.get('date'))
            if len(user) != 0:
                serializer = UserSerializer(user, many=True)
                return Response(serializer.data)
            else:
                return Response("No user were created on the requested date")
        elif self.request.query_params.get('city'):
            user = User.objects.filter(city__iexact= self.request.query_params.get('city'))
            if len(user) != 0:
                serializer = UserSerializer(user, many=True)
                return Response(serializer.data)
            else:
                return Response("No users found for requested location")

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

# class UserDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
# class UserFilter(APIView):
#
#     def get(self, request, data, format=None):
#         if re.findall('[^A-Za-z0-9]', data):
#             user = User.objects.filter(date=data)
#             if len(user) != 0:
#                 serializer = UserSerializer(user, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response("No user were created on the requested date")
#
#         else:
#             user = User.objects.filter(city__iexact=data)
#             if len(user) != 0:
#                 serializer = UserSerializer(user, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response("No users found for requested location")

















# class UserByLocation(APIView):
#     def get(self, request, location, format=None):
#         try:
#             user = User.objects.filter(city__iexact=location)
#         except User.DoesNotExist:
#             raise Http404
#         if len(user) != 0:
#             serializer = UserSerializer(user, many=True)
#             return Response(serializer.data)
#         else:
#             return Response("No users belong to asked location")
