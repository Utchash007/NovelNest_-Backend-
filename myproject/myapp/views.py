from rest_framework import viewsets
from .serializers import  UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        user_id = request.query_params.get('id', None)
        if user_id is None:
            return Response({"error": "user_id is required"}, status=500)
        user = User.objects.filter(id=user_id)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


    