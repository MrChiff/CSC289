"""
URL configuration for vgls project.

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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


# This is all of the homepage paths that django will use for the website based off of all of the different apps
# Can change the route to blog application here by adding _dev after the name
# In order to have the url pattern show up as the homepage, you will leave it '' for the path.
urlpatterns = [
    # This is the Django admin page where admins can make changes to users and groups
    path('admin/', admin.site.urls),
    # This will take you to the registeration page
    path('register/', user_views.register, name='register'),
    # This will take you to the user's profile page
    path('profile/', user_views.profile, name='profile'),
    # This will take you to the login page
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
        # This will take you to the logout page
    path('logout/', user_views.logout_view, name='logout'),
    # This will take you to the homepage of the blog app. At this time it is set as the homepage CHANGE THIS LATER!!!!!
    path('', include('blog.urls'))
]


# We are only adding this in when we are in Debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)