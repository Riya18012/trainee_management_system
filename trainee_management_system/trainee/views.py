# trainee_app/views.py
from django.shortcuts import render, redirect
from .forms import TraineeForm

def trainee_form(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TraineeForm()

    return render(request, 'trainee_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')