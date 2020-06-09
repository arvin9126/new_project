from django.db import models

class Notice(models.Model):
   title = models.CharField(max_length = 100)
   body = models.CharField(max_length = 1000)
   datetime = models.DateTimeField(auto_now=True)
   last_modified = models.DateTimeField(auto_now=False)
