from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(default = "기본 설명")
    total_score = models.IntegerField(default=0)

    def update_total_score(self):
        self.total_score = sum(score.score for score in self.score_set.all())
        self.save()
        
    total_score.short_description = "총점"
    
class Score(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.project.update_total_score()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.project.update_total_score()