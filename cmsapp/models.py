from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    deptid= models.IntegerField(primary_key=True)
    deptname= models.CharField(max_length=30)
    
    def __str__(self):
        return self.deptname

class StudentModel(models.Model):
    rno= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=30)
    dept= models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class SportModel(models.Model):
    sportid= models.IntegerField(primary_key=True)
    sportname= models.CharField(max_length=30)
    student= models.ManyToManyField(StudentModel)
    
    def __str__(self):
        return self.sportname

class InfoModel(models.Model):
    mobile= models.IntegerField(max_length=10)
    address= models.CharField(max_length=30)
    student= models.OneToOneField(StudentModel,on_delete=models.CASCADE,
        primary_key=True,)
    
    def __str__(self):
        return self.mobile