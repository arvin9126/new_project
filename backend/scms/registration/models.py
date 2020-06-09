from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
   address = models.CharField(max_length = 500)
   city = models.CharField(max_length = 50)
   state = models.CharField(max_length = 50)
   country = models.CharField(max_length = 50)
   zipcode = models.IntegerField()

class School(models.Model):
   school_name = models.CharField(max_length = 500)
   user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
   address = models.ForeignKey(Address, null=False, on_delete=models.CASCADE)
   email = models.EmailField(blank=False, null=False, unique=True)
   contactNo = models.IntegerField()

   def __str__(self):
        return self.school_name + ' - ' + self.email+ ' - ' + self.contactNo

class Studentclass(models.Model):
   section = models.CharField(max_length = 10)
   subject = models.CharField(max_length = 50)


class Teacher(models.Model):
   school = models.ForeignKey(School, null=False, on_delete=models.CASCADE)
   studentclass = models.ForeignKey(Studentclass, null=True, on_delete=models.CASCADE)
   user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   primary_skill = models.CharField(max_length = 50)
   secondary_skill = models.CharField(max_length = 50)
   address = models.ForeignKey(Address, null=False, on_delete=models.CASCADE)
   email = models.EmailField(blank=False, null=False, unique=True)
   contactNo = models.IntegerField()

   def __str__(self):
        return self.school + ' - ' + self.first_name + ' - ' + self.primary_skill + ' - ' + self.secondary_skill + ' - ' + self.contactNo + ' - ' + self.studentclass

class Student(models.Model):
   school = models.ForeignKey(School, null=False, on_delete=models.CASCADE)
   studentclass = models.ForeignKey(Studentclass, null=True, on_delete=models.CASCADE)
   user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
   student_registration_number = models.IntegerField()
   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   class_c = models.IntegerField()
   section = models.CharField(max_length = 10)
   address = models.ForeignKey(Address, null=False, on_delete=models.CASCADE)
   email = models.EmailField(blank=False, null=False, unique=True)
   contactNo = models.IntegerField()

   def __str__(self):
        return self.school + ' - ' + self.student_registration_number + ' - ' + self.class_c + ' - ' + self.contactNo + ' - ' + self.studentclass

class Parent(models.Model):
   school = models.CharField(max_length = 50)
   student_registration_number = models.IntegerField()
   user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   address = models.ForeignKey(Address, null=False, on_delete=models.CASCADE)
   email = models.EmailField(blank=False, null=False, unique=True)
   contactNo = models.IntegerField()

   def __str__(self):
        return self.school + ' - ' + self.student_registration_number + ' - ' + self.first_name + ' - ' + self.contactNo
