"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from items import views
from sendemail import views as sendmeil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repo/',include('todoapp.urls')),
    path('',views.index,name='index'),
    path('items-details/<int:pk>',views.ItemDetail.as_view(),name='item_details'),
    path('create/', views.create,name='item_create'),  
    path('edit/<int:id>', views.edit,name='item_edit'),  
    path('update/<int:id>', views.update,name='item_delete'),  
    path('update_curn/<int:id>', views.update_curn),  
    path('delete/<int:id>', views.destroy), 
    path('accounts/', include('django.contrib.auth.urls')),
    path("password_reset", sendmeil.password_reset_request, name="password_reset2"),
    ### for departr
    path('depart-list/', views.depart_create,name='depart_create'),
    path('depart-edit/<int:id>',views.depart_edit,name='depart_edit'),
    path('depart-update/<int:id>',views.depart_update,name='depart_update') ,
    path('depart-delete/<int:id>',views.depart_delete,name='depart_delete'),
    ## For Units
    path('unit-list/', views.unit_create,name='unit_create'),
    path('unit-edit/<int:id>',views.unit_edit,name='unit_edit'),
    path('unit-update/<int:id>',views.unit_update,name='unit_update') ,
    path('unit-delete/<int:id>',views.unit_delete,name='unit_delete'),



   

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
