from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    # desc = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # SCORE_CHOICES = [
    #     (1, "1점"),
    #     (2, "2점"),
    #     (3, "3점"),
    #     (4, "4점"),
    #     (5, "5점"),
    # ]

    # score = models.IntegerField(choices=SCORE_CHOICES, default=1)