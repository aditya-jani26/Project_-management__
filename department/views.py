from datetime import timezone
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt import tokens
from department.serializers import *
from department.permission import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework_simplejwt.views import BlacklistTokenView, BlacklistTokenCheckView




# Create your views here.

# ===============================-Token-==================================
class BlacklistedToken(models.Model):
    token = models.CharField(max_length=500)
    blacklisted_at = models.DateTimeField(default=timezone.now)

def get_token_for_user(user):

    refresh = RefreshToken.for_user(user)
    return {
        'Refresh_token': str(refresh),  
        'access_token': str(refresh.access_token),
    }
# =============================-RegisterView-====================================

class Register(APIView):
    def post(self, request, format=None):
        serializer = BaseuserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_token_for_user(user)
        return Response({'token':token, 'Successful': 'Registration Successful..!'}, status=status.HTTP_201_CREATED)

# ==============================-LoginView-===================================

class Login(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if user is not None:
            # Generate token using rest_framework_simplejwt
            token = tokens.AccessToken.for_user(user)
            user = Baseuser.objects.get(password=password)
            token_str = str(token)
            return Response({'token': token_str, "message": "Login Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

# ===========================-ChangePassword-======================================

class ChangePassword(APIView):  
    
    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data, context={'user' :request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"Successful":"Change Password Successful..!"}, status=status.HTTP_200_OK)
# ==============================-LogoutView-===================================
class logout(APIView):
    def post(self, request, format=None):
        token = request.data.get('token')
        
        # Create a DELETE request using Django's HttpRequest
        delete_request = HttpRequest()
        delete_request.method = 'DELETE'
        delete_request.path = '/token/blacklist/'
        delete_request.GET = {'refresh_token': token}
        
        # Call the token blacklist view with the DELETE request
        response = BlacklistTokenCheckView.BlacklistTokenView.as_view()(delete_request)
        
        # Check if the token was successfully deleted
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to logout"}, status=status.HTTP_400_BAD_REQUEST)
# ====================================-ok-=========================================