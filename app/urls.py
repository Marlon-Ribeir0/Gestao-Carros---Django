from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from carros.views import CarrosListView, NovoCarroCreateView, carroDetales, carroAtualizar, carroApagar
from contas.views import cadastro_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cadastros/", cadastro_view, name="cadastro"),
    path('carros/', CarrosListView.as_view(), name='carro_lista'),
    path('novo_carro/', NovoCarroCreateView.as_view(), name='novo_carro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('detalhes/<int:pk>', carroDetales.as_view(), name='detalhes'),
    path('detalhes/<int:pk>/atualizar/', carroAtualizar.as_view(), name='carro_atualizar'),
    path('detalhes/<int:pk>/apagar/', carroApagar.as_view(), name='carro_apagar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
