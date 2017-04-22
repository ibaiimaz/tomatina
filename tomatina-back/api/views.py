from django.contrib.auth.models import Group
from rest_framework import viewsets
from api.models import Pomodoro
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from api.serializers import (
    UserSerializer,
    GroupSerializer,
    UserStatusSerializer,
    TeamStatusSerializer
)
User = get_user_model()



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pomodoro.objects.all()
    serializer_class = UserStatusSerializer

    def retrieve(self, request, *args, **kwargs):
        return super(UserStatusViewSet, self).retrieve(
            request, *args, **kwargs)


class UserStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pomodoro.objects.all()
    serializer_class = UserStatusSerializer

    def retrieve(self, request, *args, **kwargs):
        now = timezone.now()
        pomodoros = Pomodoro.objects.filter(
            user_id=kwargs['pk'],
            started__gte= timezone.datetime(month=now.month, year=now.year, day=now.day)
        ).order_by('-started')
        return super(UserStatusViewSet, self).retrieve(request, *args, **kwargs)


class TeamStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Pomodoro.objects.all()
    serializer_class = TeamStatusSerializer

    def retrieve(self, request, *args, **kwargs):
        Pomodoro.objects.filter(user_id=kwargs['pk'], started__gte=timezone.now()).order_by('-started')
        return super(TeamStatusViewSet, self).retrieve(request, *args, **kwargs)
