"""
URL configuration for sistema project.

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
from django.urls import path
from apk.views import convertir_pdf_a_imagen, vista

urlpatterns = [
    path('convertir-pdf-a-imagen/', convertir_pdf_a_imagen, name='convertir_pdf_a_imagen'),
    path('vista/', vista, name="vista")
    # Otras URLs de tu aplicación...
]
