from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.core.exceptions import SuspiciousOperation
from .models import Usuarios
from django.core.mail import send_mail
from django.template.loader import render_to_string




class Home(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Inicio(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name) 
    
class power(APIView):
    template_name="dashboard.html"
    def get(self,request):
        return render(request,self.template_name) 
    
# class Usuario:
#     def Usuari(self, nombre, correo, contraseña):
#         self.nombre = nombre
#         self.correo = correo
#         self.contraseña = contraseña  
# hasta 
    
def registro(request):
    if request.method == 'POST':
        nom = request.POST['usuario']
        contra = request.POST['pass']
        corr = request.POST['email']
        # matri = request.POST['matricula']
        
        # Verificar si el correo ya está registrado
        if Usuarios.objects.filter(correo=corr).exists():
            messages.error(request, 'El correo ya está registrado')
            return render(request, 'login.html')  # Cambia 'registro.html' al nombre correcto de tu página de registro
        
        Usuarios(usuario=nom, correo=corr, contraseña=contra).save()
        messages.success(request, 'Usuario registrado exitosamente')

        # Verificacion de correo
        subject = 'Verficación del correo!'
        message = f"!Gracias por unirte a nuestra página. Por favor haz click en el siguiente enlace para verificar tu correo! "
        from_email = "gabrielm1877@gmail.com"
        send_mail(subject, message, from_email, [corr])
        messages.success(request, "Usuario registrado correctamente, Por favor verifica tu correo!")
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
 
 #----------------------------------------------------------------       
        
def inicio_de_sesion(request):
    if request.method == 'POST':
        correo1   = request.POST.get('correoFo')
        contraseña1  = request.POST.get('passFo')
        
        try:
            user = Usuarios.objects.get(correo=correo1, contraseña=contraseña1)
            request.session['correo'] = user.correo

            return redirect('index')
        except Usuarios.DoesNotExist:
            messages.error(request, 'User does not exist!')
        except Usuarios.MultipleObjectsReturned:
            messages.error(request, 'Multiples users with the same name!')

    return render(request, 'login.html')
      