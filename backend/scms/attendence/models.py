from django.db import models
from registration.models import Teacher, Student, Studentclass

class Attendence(models.Model):
   teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
   studentclass = models.ForeignKey(Studentclass, null=False, on_delete=models.CASCADE)
   attendence = models.CharField(max_length = 10)
   datetime = models.DateTimeField(auto_now=True)

   def __str__(self):
        return self.student + ' - ' + self.studentclass+ ' - ' + self.attendence


