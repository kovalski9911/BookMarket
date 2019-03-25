from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.http import Http404


from .permissions import IsOwnerOrIsStaffPermission, IsStaffOnly
from .serializers import UserSerializer, RegisterUserSerializer


User = get_user_model()


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsStaffOnly, ))
def users_list_api_view(request):
    """List of all profiles"""
    users = User.objects.all()
    data = UserSerializer(users, many=True).data
    return Response(data)


class UserDetailApiView(APIView):
    permission_classes = (IsAuthenticated, IsOwnerOrIsStaffPermission, )

    # def get_object(self, pk):
    #     print('get_object is worked')
    #     try:
    #         return User.objects.get(pk=pk)
    #     except User.DoesNotExist:
    #         raise Http404

    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
