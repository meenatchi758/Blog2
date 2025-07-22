from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bug
from .forms import BugForm

@login_required
def submit_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.reported_by = request.user
            bug.save()
            return redirect('my_bugs')
    else:
        form = BugForm()
    return render(request, 'bugs/submit_bug.html', {'form': form})

@login_required
def my_bugs(request):
    bugs = Bug.objects.filter(reported_by=request.user)
    return render(request, 'bugs/my_bugs.html', {'bugs': bugs})

@login_required
def all_bugs(request):
    bugs = Bug.objects.all()
    return render(request, 'bugs/all_bugs.html', {'bugs': bugs})

@login_required
def update_status(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        bug.status = status
        bug.save()
        return redirect('all_bugs')
    return render(request, 'bugs/update_status.html', {'bug': bug})


def home(request):
    return render(request, 'home.html')   # create this template
