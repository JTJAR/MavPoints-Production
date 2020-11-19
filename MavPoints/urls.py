from django.conf.urls import url
from . import views
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import SignUpView

app_name = 'MavPoints'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('promotions', views.promotions, name='promotions'),
    path('contact', views.contact, name='contact'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('rewards', views.rewards, name='rewards'),
    path('employee_home', views.home_employee, name='employee_home'),
    path('view_customers', views.view_customers, name='view_customers'),
    path('account/create/', SignUpView.as_view(), name='create_account'),
    path('customer/<int:pk>/edit/', views.edit_customer, name='edit_customer'),
    path('customer/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
