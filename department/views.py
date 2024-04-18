from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt import tokens
from department.serializers import *
from department.permission import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# ===============================-Token-==================================

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
        
        # Custom check_password function
        user = self.check_password(email, password)
        
        if user is not None:
            # Generate token using rest_framework_simplejwt
            token = tokens.AccessToken.for_user(user)
            token_str = str(token)  # Convert AccessToken object to string
            return Response({'token': token_str, "message": "Login Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def check_password(self, email, password):

        try:
            user = Baseuser.objects.get(email=email)
            if check_password(password, user.password):  
                return user
            else:
                return None
        except Baseuser.DoesNotExist:
            return None
# =================================================================
class ChangePassword(APIView):  
    permission_classes=[IsAuthenticated]
    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data, context={'user' :request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"Successful":"Change Password Successful..!"}, status=status.HTTP_200_OK)
    



# ==============================-LogoutView-===================================

# class logout(APIView):
#     def post(self, request, format=None):
#         token = request.data.get('token')
        
#         # Blacklist the token using rest_framework_simplejwt's built-in view
#         response = blacklist_views.BlacklistTokenView.as_view()(request)
        
#         return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)