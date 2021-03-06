"""corona_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from corona_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^data/', views.dataList.as_view()),
]
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views as rfviews

from corona_app import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'currentSituation', views.CoronaDataCurrentViewSet)
router.register(r'data', views.CoronaDataViewSet)
router.register(r'countryDataList', views.CountryDataViewSet)
router.register(r'dateCaseDataList', views.DateCaseViewSet)
router.register(r'DateDeathDataList', views.DateDeathViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/',rfviews.obtain_auth_token, name='api-token-auth'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]