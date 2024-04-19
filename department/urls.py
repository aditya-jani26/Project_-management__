from django.urls import path
from .views import *

urlpatterns = [

    path('RegisterView/', RegisterView.as_view(), name="RegisterView"),
    path('LoginView/', LoginView.as_view(), name="LoginView"),
    path('ChangePassword/', ChangePassword.as_view(), name="ChangePasswordView"),
    
#     path('logout/', Logout.as_view(), name="logout"),
#     path('department/', DepartmentView.as_view(), name="department"),
#     path('department/<int:pk>/', DepartmentDetailView.as_view(), name="department_detail"),
#     path('department/<int:pk>/update/', DepartmentUpdateView.as_view(), name="department_update"),

]
