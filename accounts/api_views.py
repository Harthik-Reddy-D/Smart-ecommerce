from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import User
from .permissions import IsAdmin, IsStaffOrAdmin
from .serializers import RegisterSerializer, UserSerializer, RoleSerializer, EmailTokenSerializer

class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginAPI(TokenObtainPairView):
    serializer_class = EmailTokenSerializer

class RefreshAPI(TokenRefreshView):
    pass

class MeAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user

class UserAdminAPI(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = RoleSerializer
    permission_classes = [IsAdmin]

class UserAdminDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdmin]

class StaffPingAPI(APIView):
    permission_classes = [IsStaffOrAdmin]
    def get(self, request):
        return Response({"status": "staff-ok"})
