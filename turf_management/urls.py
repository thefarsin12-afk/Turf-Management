"""
URL configuration for turf_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from turf_booking.views import AdminRegister
from turf_booking.views import TurfListCreateView,TurfRetrieveUpdateDeleteView
from turf_team_register.views import TurfRegisterListCreate

urlpatterns = [
    path('admin/', admin.site.urls),

    # turf record booking rough
    path('admin-register/',AdminRegister.as_view()),
    path('turf/',TurfListCreateView.as_view()),
    path("turf/<int:pk>/",TurfRetrieveUpdateDeleteView.as_view()),

    # turf team register booking rough
    path("register/",TurfRegisterListCreate.as_view()),
]
