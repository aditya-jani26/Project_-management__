from django.db import models
from django.utils.timezone import now

class Baseuser(models.Model):
    userType = models.CharField(max_length=100, choices=(('Employee', 'Employee'), ('Project-Manager', 'Project-Manager'), ('Team-Leader', 'Team-Leader'), ('Admin', 'Admin')))
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    allocation_percentage = models.IntegerField(default=0)

class Project(models.Model):
    projectCreator = models.ForeignKey(Baseuser, on_delete=models.CASCADE)
    project_id = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=50)
    projectDescription = models.CharField(max_length=500)
    project_assigned_on = models.DateTimeField(default=now)
    projectStartDate = models.DateField(default=project_assigned_on)
    projectEndDate = models.DateField(null=True)
    toDo = models.CharField(max_length=100, choices=(('In progress', 'In progress'),('Completed', 'Completed')))