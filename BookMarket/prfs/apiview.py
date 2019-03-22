from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from  rest_framework.permissions import AllowAny,

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, RegisterUserSerializer


User = get_user_model()


@api_view(['GET'])
def users_list_api_view(request):
    """List of all profiles"""
    users = User.objects.all()
    data = UserSerializer(users, many=True).data
    return Response(data)


# @api_view(['PUT', 'GET'])
# # @permission_classes((IsAuthenticated,))
# def users_update_api_view(request, pk):
#     """Update prfl"""
#     user = User.objects.get(pk=pk)
#     if request.method == 'PUT':
#         data = UserSerializer(data=request.data)
#         if data.is_valid():
#             data.save()
#             return Response(data.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def register_user_api_view(request):
    """register users"""
    user = RegisterUserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def login_user_api_view(request):
    """login users"""
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
