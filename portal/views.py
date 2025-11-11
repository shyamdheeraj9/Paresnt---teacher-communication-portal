from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Class, Attendance, Grade

@login_required
def dashboard(request):
    # Example: Show classes and messages
    classes = Class.objects.filter(teacher=request.user.teacher)
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'portal/dashboard.html', {'classes': classes, 'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        # Handle sending message logic
        pass
    return render(request, 'portal/send_message.html')
