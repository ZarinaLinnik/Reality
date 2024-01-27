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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import main.views as main_views
import main.errors as main_errors

urlpatterns = [
    path('', main_views.start, name='start'),  # Start page
    path('admin/', admin.site.urls),  # Administrative panel
    path('registration/', main_views.registration, name='registration'),  # User registration
    path('who_are_you/', main_views.add_parameter1_who_are_you, name='who_are_you'), # Parameter 1 Who Are You
    path('what_do_you_do/', main_views.add_parameter2_what_do_you_do, name='what_do_you_do'),  # Parameter 2 What Do You Do
    path('environment/', main_views.add_parameter3_environment, name='environment'),  # Parameter 3 Environment
    path('habits/', main_views.add_parameter4_habits, name='habits'),  # Parameter 4 Habits
    path('free_time/', main_views.add_parameter5_free_time, name='free_time'),  # Parameter 5 Free Time
    path('appearance/', main_views.add_parameter6_appearance, name='appearance'),  # Parameter 6 Appearance
    path('behavior/', main_views.add_parameter7_behavior, name='behavior'),  # Parameter 7 Behavior
    path('mind/', main_views.add_parameter8_mind, name='mind'),  # Parameter 8 Mind
    path('my_photo/', main_views.my_photo, name='my_photo'),  # Page with user's photo and its date&time
    path('accounts/profile/', main_views.creature, name='creature'),  # Main account page
    path('feedback/', main_views.feedback, name='feedback'),  # User can leave feedback
    path('delete_account/', main_views.delete_account, name='delete_account'),  # User delete user's account
    path('400/', main_errors.error400),  # Error 400
    path('403/', main_errors.error403),  # Error 403
    path('404/', main_errors.error404),  # Error 404
    path('405/', main_errors.error405),  # Error 405
    path('500/', main_errors.error500),  # Error 500
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'), name='authorization'),  # include django paths
    path('logout/', main_views.log_out, name='logout'),  # Log out possibility
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Connection static path

handler400 = 'main.errors.error400'  # 400 error handler
handler403 = 'main.errors.error403'  # 403 error handler
handler404 = 'main.errors.error404'  # 404 error handler
handler405 = 'main.errors.error405'  # 405 error handler
handler500 = 'main.errors.error500'  # 500 error handler
