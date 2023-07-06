from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from rest_framework.views import APIView


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')  # admin1
    password = request.data.get('password')  # 1234

    user = User.objects.create_user(username=username, password=password)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})


class AuthorizationAPIView(APIView):
    def post(self, request):
        # Step 1: Get creadential data from client
        username = request.data.get('username')
        password = request.data.get('password')

        # Step 2: Authentication of user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Step 3: Return Key
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        else:
            # Step 4: Return error
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'User credentials not correct!'})