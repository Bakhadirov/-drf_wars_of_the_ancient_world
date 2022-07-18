from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from main_app.apps.users.api.serializers.user import UserSerializer, UserUpdateSerializer
from main_app.apps.users.models import User


class UserRegistrationView(CreateAPIView):
    model = User
    authentication_classes = ()
    serializer_class = UserSerializer


@extend_schema_view(get=extend_schema(responses={200: UserSerializer}))
class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,) # TODO добавить в дальнейшем просмотр юзеров только для админов?

    def get(self, request: Request, *args, **kwargs) -> Response:
        return Response(UserSerializer(self.request.user).data)

    def patch(self, request, *args, **kwargs):
        instance = self.request.user

        serializer = UserUpdateSerializer(instance, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'user': serializer.data})



