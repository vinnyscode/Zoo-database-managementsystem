"""zoodatabase URL Configuration

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
from django.urls import path
from zooapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StaffData/', StaffData),
    path('savedata/', savedata),

    path('VisitorData/',VisitorData),
    path('datasave/', datasave),

    path('TicketData/',TicketData),
    path('saveddata/', saveddata),

    path('SpeciesData/',SpeciesData),
    path('datasaved/', datasaved),

    path('AnimalData/',AnimalData),
    path('datasaving/', datasaving),

    path('LooksAfterData/',LooksAfterData),
    path('savingdata/', savingdata)

]