from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

# Create your views here.

User = get_user_model()

def signup(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        email = request.POST['email'].strip()

        if not username:
            errors['username'] = 'Username is required'
        elif len(username) < 6:
            errors['username'] = 'Username must be at least 6 characters'
        elif len(username) > 20:
            errors['username'] = 'Username must be at most 20 characters'
        else:
            is_used = User.objects.filter(username=username).exists()
            if is_used:
                errors['username'] = 'Username is already used!'

        if not password1:
            errors['password1'] = 'Password is required' 
        elif len(password1) < 8:
            errors['password1'] = 'Password must be at least 8 characters'
        elif len(password1) > 20:
            errors['password1'] = 'Password must be at most 20 characters'    

        if not password2:
            errors['password2'] = 'Password confirmation is required'
        elif password1 != password2:
            errors['password2'] = 'Passwords do not match!!'

        if not first_name:
            errors['first_name'] = 'First name is required'

        if not email:
            errors['email'] = 'Email is required'    
        elif not email.endswith('@gmail.com'):
            errors['email'] = 'Email must be a gmail account'
        elif User.objects.filter(email=email).exists():
            errors['email'] = 'Email is already used!'

        is_valid = not errors

        if is_valid:
            user = User.objects.create_user(
                username=username, 
                password=password1, 
                first_name=first_name, 
                last_name=last_name, 
                email=email
            )
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('/?signup=success')
        
    context={
        'errors': errors
    }
    
    return render(request, 'registration/signup.html', context)