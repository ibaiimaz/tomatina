from django.contrib.auth.models import Group
from rest_framework import viewsets
from api.models import Pomodoro
from rest_framework.response import Response
from api.serializers import (
    UserSerializer,
    GroupSerializer,
    UserStatusSerializer,
    TeamStatusSerializer
)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


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
        return super(UserStatusViewSet, self).retrieve(
            request, *args, **kwargs)


class TeamStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Pomodoro.objects.all()
    serializer_class = TeamStatusSerializer

    def retrieve(self, request, *args, **kwargs):
        kwargs['pk']
        return super(TeamStatusViewSet, self).retrieve(
            request, *args, **kwargs)
