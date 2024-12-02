from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def cadastro_view(request):
    if request.method == "POST":
        usuario_form = UserCreationForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('login')
    else:
        usuario_form = UserCreationForm()
    return render(
        request,
        'cadastro.html',
        { 'cadastro_user' : usuario_form  }
    )



def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user1 = authenticate(request, username=username, password=password)
        if user1 is not None:
            login(request, user1)
            return redirect('carro_lista')
        else:
            login_form = AuthenticationForm(request, data=request.POST)


            
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login' : login_form})




def logout_view(request):
    logout(request)
    return redirect('carro_lista')
