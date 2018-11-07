from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# urls de la aplicación /sitio 

urlpatterns = [
    path('', views.home, name="home"),
    #usuario
    #path('user/', views.user_detail, name='user_detail'),
    path('user/', views.user_profile, name='user_profile'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/login/', views.user_login, name="user_login"),
    path('user/logout/', views.user_logout, name="user_logout"),

    #perro
    path('perros/lista/', views.perros_todos, name='perros'),
    path('perros/rescatados/', views.perros_rescatados, name='perros_rescatados'),
    path('perros/disponibles/', views.perros_disponibles, name='perros_disponibles'),
    path('perros/adoptados/', views.perros_adoptados, name='perros_adoptados'),
    #perros de detalles

    path('perros/lista/perro/<int:pk>/', views.perros_detail, name='perros_detail'),
    path('perros/lista/perro/new/', views.perros_new, name='perros_new'),
    path('perros/lista/perro/<int:pk>/edit/', views.perros_edit, name='perros_edit'),
    path('perros/lista/perro/<int:pk>/delete/', views.perros_delete, name='perros_delete'),
    path('perros/lista/perro/<int:pk>/update/', views.perros_update, name='perros_update'),
    
    #recuperrar contraseña //template en email omitidos
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)