from datetime import timezone
from django.shortcuts import get_object_or_404

from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt import tokens
from department.serializers import *
from department.permission import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from rest_framework.permissions import AllowAny

# ===============================-Token-==================================

class BlacklistedToken(models.Model):
    token = models.CharField(max_length=500)
    # blacklisted_at = models.DateTimeField(default=timezone.now)

def get_token_for_user(user):

    refresh = RefreshToken.for_user(user)
    return {
        'Refresh_token': str(refresh),  
        'access_token': str(refresh.access_token),
    }

# =============================-RegisterView-====================================

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Successful': 'Registration Successful..!'}, status=status.HTTP_201_CREATED)

# ==============================-LoginView-===================================

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        print(email,"ok")
        password = serializer.data.get('password')
        print(password,"ok")
        userType = serializer.data.get('userType')
        login_user = CustomUser.objects.get(email=email)
        if userType == 'Admin': 
            user = authenticate(email=email, password=password )
        else:
            user = check_password(password,login_user.password)
        print(user,"ok")
        if user is not None:
            token = get_token_for_user(user)
            return Response({'token':token, "Successful":"Login Successful..!"}, status=status.HTTP_200_OK)
        else:
            return Response({'"error":"no it was not Successful":"Login Successful..!"'}, status=status.HTTP_401_UNAUTHORIZED)    
                
            
# ===========================-ChangePassword-======================================

class ChangePassword(APIView):  
    
    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data, context={'user' :request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"Successful":"Change Password Successful..!"}, status=status.HTTP_200_OK)
    
# ==============================-LogoutView-===================================
    
# class logout(APIView):
#     def post(self, request, format=None):
#         token = request.data.get('token')
        
#         # Create a DELETE request using Django's HttpRequest
#         delete_request = HttpRequest()
#         delete_request.method = 'DELETE'
#         delete_request.path = '/token/blacklist/'
#         delete_request.GET = {'refresh_token': token}
        
#         # Call the token blacklist view with the DELETE request
#         response = BlacklistTokenCheckView.BlacklistTokenView.as_view()(delete_request)
        
#         # Check if the token was successfully deleted
#         if response.status_code == status.HTTP_204_NO_CONTENT:
#             return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Failed to logout"}, status=status.HTTP_400_BAD_REQUEST)
        
# ====================================-ok-=========================================