from django.contrib import admin
from .models import Project, Score

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'total_score')
    ordering = ('-total_score',)
    readonly_fields = ('total_score',)
    
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'score')
    list_filter = ('project',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Score, ScoreAdmin)