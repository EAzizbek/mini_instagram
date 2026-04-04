from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

User = get_user_model()

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login') # Ro'yxatdan o'tgach login sahifasiga yuboradi

def user_profile(request, pk):
    user_obj = get_object_or_404(User, pk=pk)
    user_posts = user_obj.posts.all().order_by('-created_at')
    
    context = {
        'user_obj': user_obj,
        'user_posts': user_posts,
    }
    return render(request, 'users/user_profile.html', context)
