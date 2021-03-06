"""tomatina URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'pomodoro', views.PomodoroViewSet)
router.register(r'user-status', views.UserStatusViewSet, base_name='user-status')
router.register(r'team-status', views.TeamStatusViewSet, base_name='team-status')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
