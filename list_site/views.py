from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Score

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        score_value = int(request.POST.get('score'))
        Score.objects.create(project=project, score=score_value)
        return redirect('project_list')  # ⬅️ 목록 페이지로 이동
    
    return render(request, 'project_detail.html', {'project': project})