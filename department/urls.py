from django.urls import path
from .views import *

urlpatterns = [

    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('ChangePassword/', ChangePassword.as_view(), name="ChangePasswordView"),
    path('logout/', Logout.as_view(), name="logout"),
#     path('department/', DepartmentView.as_view(), name="department"),
#     path('department/<int:pk>/', DepartmentDetailView.as_view(), name="department_detail"),
#     path('department/<int:pk>/update/', DepartmentUpdateView.as_view(), name="department_update"),

]
