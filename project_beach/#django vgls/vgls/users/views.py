from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



##########################
# Register Page Function #
##########################
# This will handle the traffic to the user registration form.
# Will see if there is a post request then will send information to the Post table in the database

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



########################
# Logout Page Function #
########################
# This will log the user out of the program.
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')



#########################
# Profile Page Function #
#########################
# The user must be logged in to be able to see the profile page
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:  
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)  
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)