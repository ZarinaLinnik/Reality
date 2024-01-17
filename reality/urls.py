"""
URL configuration for reality project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main_views

urlpatterns = [
    path('400/', main_views.error400),
    path('403/', main_views.error403),
    path('404/', main_views.error404),
    path('405/', main_views.error405),
    path('500/', main_views.error500),
    path('', main_views.start),
    path('admin/', admin.site.urls),
    path('registration/', main_views.registration, name='registration'),
    path('who_are_you/', main_views.add_parameter1_who_are_you, name='who_are_you'),
    path('my_photo/', main_views.my_photo, name='my_photo'),
    path('accounts/profile/', main_views.creature, name='creature'),
    path('feedback/', main_views.feedback, name='feedback'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'), name='authorization'),
    path('logout/', main_views.log_out, name='logout'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'main.views.error400'
handler403 = 'main.views.error403'
handler404 = 'main.views.error404'
handler405 = 'main.views.error405'
handler500 = 'main.views.error500'
