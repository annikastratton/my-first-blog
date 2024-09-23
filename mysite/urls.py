"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls

'''
https://tutorial-extensions.djangogirls.org/en/add_wagtail_to_your_website/install_wagtail/

Wagtail comes with its own custom admin interface provided by wagtailadmin_urls 
which we will be able to access by visiting the URL/cms/. This is different from the 
Django admin interface provided by django.contrib.admin we have been accessing by the
 /admin/ URL. In a typical Wagtail only project, the admin site would be at /admin/ 
 but because we are adding Wagtail to an already existing Django project, this would 
 clash with our admin URL, so we are using /cms/ to access the Wagtail admin interface 
 and keep using /admin/ to access the Django admin interface.
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('blog/', include('blog.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
