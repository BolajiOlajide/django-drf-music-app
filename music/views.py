from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from music.models import Song
from music.serializers import SongSerializer, TokenSerializer


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class ListSongsView(ListAPIView):
    """
    Provides a get method handler.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LoginView(CreateAPIView):
    """
    POST auth/login/
    """

    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(
                data={
                    # using drf jwt utility functions to generate a token
                    "token": jwt_encode_handler(jwt_payload_handler(user))
                }
            )
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsersView(CreateAPIView):
    """
    POST auth/register/
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        login(request, new_user)
        serializer = TokenSerializer(
            data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(jwt_payload_handler(new_user))
            }
        )
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
