from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from usuarios.forms import RegistroForm

@login_required(login_url="/usuarios/login")
def perfil(request):
    return render(request, 'perfil.html')

# Bloquear vista a usuarios logueados
@user_passes_test(lambda u: u.is_anonymous, login_url="/usuarios/")
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, 'registro.html', context)
    form = RegistroForm(request.POST or None)
    context = {"form": form}
    return render(request, 'registro.html', context)

def login(request):
    if request.method == "POST":
        if 'correo' in request.POST.keys() and 'clave' in request.POST.keys():
            user = auth.authenticate(username=request.POST["correo"],password=request.POST["clave"])
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect("/")
            else:
                context = {"message": "Usuario o contraseña incorrecto", "alert": "danger"}
                return render(request, 'login.html', context)
        else:
            context = {"message": "error"}
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

# Create your views here.
