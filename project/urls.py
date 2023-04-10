"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from main.views import *
from django.conf.urls.static import static
from project.settings import MEDIA_ROOT,MEDIA_URL
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='home'),
    path('abaut', abaut,name='abaut'),
    path('det/<int:id>',detail,name='detail'),
    path('favorites/<int:id>',favorites,name='favorites'),
    path('favorite',favorites_page,name='favorites_page'),
    path('remove_form/<int:id>',remove_form,name='remove_form'),

    path('cart/<int:id>', cart, name='cart'),
    path('cartpage/', cart_page, name='cartpage'),
    path('delete/<int:id>', delete, name='deleete'),

    path('auth/', authen,name='auth'),
    path('sign_up/', sign_up,name='sign_up'),
    path('logout', logout,name='logout'),
    path('order/', order,name='order'),
]


urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)