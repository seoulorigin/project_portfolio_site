from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(default = "기본 설명")
    
class Score(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField()