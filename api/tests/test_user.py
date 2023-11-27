import pytest

set.DJANGO.SETTINGS.MODULE = API_DJANGO_C.settings


from api.models import Usuarios

@pytest.mark.django_db
def test_user_creation():
    user = Usuarios.objects.create_user(
       usuario = 'Ale',
       contraseña = '12345',
       correo = 'Ale@gmail.com' 
    )
    assert user.usuario == 'Ale'