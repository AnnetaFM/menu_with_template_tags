from django.contrib import admin
from django.urls import path
from menu_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/draw_menu/<str:menu_name>/', views.draw_menu, name='draw_menu'),
]
