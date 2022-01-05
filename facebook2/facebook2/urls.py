
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('profile/', views.profile),
    path('post/', views.post),
    path('notice/', views.notice),
    path('notice/<int:id>', views.notice),
]
