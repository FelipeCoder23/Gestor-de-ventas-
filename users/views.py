from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from pyexpat.errors import messages

# Create your views here.


def login_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Guardar el usuario y obtener el objeto user
            user = form.save()
            print("se guardo")
            print(user.role)
            # Autenticar al usuario
            authenticated_user = authenticate(username=user.username, password=request.POST["password1"])
            
            if authenticated_user:
                # Si la autenticación es exitosa, hacer login
                login(request, authenticated_user)
                
                # Redirigir según el tipo de usuario
                if user.role == "jefe":
                    return redirect("jefe")
                else:
                    return redirect("empleado")
            else:
                # Manejo del error de autenticación
                return render(request, "inicio2.html", {"form": form, "error": "Autenticación fallida después de crear la cuenta."})
            
        else:
            return render(request, "inicio2.html", {
                "form": form
            })
    else:
        form = CustomUserCreationForm()
        return render(request, "inicio2.html", {
            "form": form
        })

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # El formulario ya tiene la lógica para validar las credenciales
            # Así que simplemente obtenemos el usuario
            user = form.get_user()

            # Hacer login
            login(request, user)
            
            # Redirigir según el tipo de usuario
            if user.role == "jefe":
                return redirect("jefe")
            else:
                return redirect("empleado")
        else:
            # Si las credenciales no son válidas, muestra el formulario nuevamente con los errores
            return render(request, "home.html", {"form": form})
    else:
        return render(request, "home.html", {
            "form": AuthenticationForm()
        })



def jefe(request):
    return render(request, "jefe.html")

def empleado(request):
    return render(request, "empleado.html")


