from django.shortcuts import render, redirect


def register(request):
  if request.method == 'POST':
    print('submitted reg')
    return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    print('submitted login')
    return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')
