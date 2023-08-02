from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone

class Building(models.Model):
    building = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.building}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='')

    def __str__(self):
         return f"{self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
         return f"{self.first_name} {self.last_name}, Id: {self.student_id}"

class Destination(models.Model):
    # thing = models.CharField(max_length=200, default="") # test for race condition
    building = models.ForeignKey(Building, null=True, on_delete=models.SET_NULL)
    room = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    max_people_allowed = models.PositiveIntegerField(default = 2)

    def __str__(self):
         if (self.category):
            return f"{self.room} {self.category.name}"
         return f"{self.room} Genderless"
    

class Log(models.Model):
    Time_in = models.DateTimeField(auto_now=True)
    Time_out = models.DateTimeField(blank=True, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        permissions = (("can_view_log_history", "can_edit_log_history"),)

    def __str__(self):  
            self.Time_in = datetime.now()
           
            return f"Teacher: {self.user}, Destination: {self.destination}, Student: {self.student_id}, Time_in: {self.Time_in}, Time_out: x{self.Time_out} "

class Profile(models.Model):
    destination = models.ForeignKey(Destination, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    building = models.ForeignKey(Building, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user}, {self.building},"