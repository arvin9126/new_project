from django.db import models
from registration.models import Teacher, Student
from attendence.models import Studentclass

class Exam(models.Model):
   teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
   studentclass = models.ForeignKey(Studentclass, null=False, on_delete=models.CASCADE)
   exam_name = models.CharField(max_length = 50)
   status = models.CharField(max_length = 10)
   datetime = models.DateTimeField(auto_now=False)
   total_score = models.IntegerField()
   remarks = models.CharField(max_length = 50)

   def __str__(self):
        return self.teacher + ' - ' + self.student + ' - ' + self.studentclass + ' - ' + self.exam_name + ' - ' + self.total_score


class Questionset(models.Model):
   question = models.CharField(max_length = 500)
   answer = models.CharField(max_length = 100)
   option1 = models.CharField(max_length = 100)
   option2 = models.CharField(max_length = 100)
   option3 = models.CharField(max_length = 100)
   option4 = models.CharField(max_length = 100)


class Scorecard(models.Model):
   exam = models.ForeignKey(Exam, null=False, on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
   studentclass = models.ForeignKey(Studentclass, null=False, on_delete=models.CASCADE)
   datetime = models.DateTimeField(auto_now=True)

   def __str__(self):
        return self.student+ ' - ' + self.studentclass + ' - ' + self.exam


