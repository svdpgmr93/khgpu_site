"""
URL configuration for hgpu_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('index/', index),
    # Меню УНИВЕРСИТЕТ
    # -- START --
    path('sveden/', sveden, name='sveden'),
    # -- END --
    # Сведения об образовательной организации 
    # -- START --
    path('sveden/common', common, name='common'),
    path('sveden/struct', struct, name='struct'),
    path('sveden/document', document,  name='document'),
    path('sveden/education', education, name='education'),
    path('sveden/education/mag_opop', mag_opop, name='mag_opop'),
    path('sveden/eduStandarts', eduStandarts, name='eduStandarts'),
    path('sveden/managers', managers, name='managers'),
    path('sveden/employees', employees, name='employees'),
    path('sveden/objects', objects, name='objects'),
    path('sveden/grants', grants, name='grants'),
    path('sveden/paid_edu', paid_edu, name='paid_edu'),
    path('sveden/budget', budget, name='budget'),
    path('sveden/vacant', vacant, name='vacant'),
    path('sveden/inter', inter, name='inter'),
    path('sveden/catering', catering, name='catering'),
    path('test', test, name='test'),
    # -- END --
]
