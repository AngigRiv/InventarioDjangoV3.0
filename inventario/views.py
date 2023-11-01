from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from inventario.forms import LoginForm
from inventario.models import Marca, UnidadMedida

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Crea una instancia del formulario con los datos POST
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Contraseña o correo incorrectos.')
        else:
            messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')

    else:
        # El formulario de autenticación maneja automáticamente las credenciales incorrectas
        # Sin embargo, puedes mostrar un mensaje de error personalizado si lo deseas.
        form = LoginForm()  # Si es una solicitud GET, crea un formulario en blanco
    return render(request, 'plantilla/login.html', {'form': form})

def index(request):
    num_Marca= Marca.objects.all().count()
    num_UnidadMedida=UnidadMedida.objects.all().count()

    context = {
        'num_Marca' : num_Marca,
        'num_UnidadMedida':num_UnidadMedida,
    }
    return render(request,'inicio.html',context=context)
    

def logout_user(request):
    logout(request)
    return redirect('login')