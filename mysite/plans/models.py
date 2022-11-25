from django.db import models

# Create your models here.
class Plan(models.Model):
    plan_id=models.IntegerField()
    plan_title=models.TextField()
    plan_content=models.TextField()
    plan_desc=models.TextField()
    plan_time=models.TextField()