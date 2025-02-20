from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# from backend.models import Task
from .permissions import IsEmployee
from .serializers import UserSerializer


# from .serialiers import UserSerializer, TaskSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

# class ListTask(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self, request):
#         task = Task.objects.all()
#         # serializer = TaskSerializer(task, many=True)
#         return Response(serializer.data)
#
# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# @permission_classes([IsEmployee])
# def list_todo(request):
#     task = Task.objects.all()
#     serializer = TaskSerializer(task, many=True)
#     return Response(serializer.data)