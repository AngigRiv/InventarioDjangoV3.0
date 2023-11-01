from django.urls import include,path
from .views import login_user,index,logout_user
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_user, name='login'),
    path('inicio', login_required(index), name='index'),  # Ruta de inicio protegida     
    path('logout',logout_user, name='logout'),
    path('marcas/', include('marcas.urls')),
    path('empresas/', include('empresas.urls')),
    path('sucursales/', include('sucursales.urls')),
    path('personales/', include('personales.urls')),
    path('inventarios_A/', include('inventarios_A.urls')),
    path('unidades/', include('unidades.urls')),
    path('grupos/', include('grupos.urls')),
    path('lineas/', include('lineas.urls')),
    path('sublineas/', include('sublineas.urls')),
    path('articulos/', include('articulos.urls')),
]
