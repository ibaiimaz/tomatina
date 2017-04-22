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
    ListUsersSerializer,
    PomodoroSerializer
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
    filter_fields = ('username',)

    def perform_create(self, serializer):

        super(UserViewSet, self).perform_create(serializer)


class PomodoroViewSet(viewsets.ModelViewSet):
    queryset = Pomodoro.objects.all()
    serializer_class = PomodoroSerializer


class UserStatusViewSet(viewsets.ModelViewSet):
    queryset = Pomodoro.objects.all()
    serializer_class = UserStatusSerializer

    def retrieve(self, request, *args, **kwargs):
        now = timezone.now()
        pomodoros = Pomodoro.objects.filter(
            user_id=kwargs['pk'],
            started__gte= timezone.datetime(month=now.month, year=now.year, day=now.day)
        ).order_by('-started')
        #self.get_serializer()()
        #serializer = self.get_serializer(instance)
        return Response({'status':12, 'started':21, 'pomodoros':12})


class TeamStatusViewSet(viewsets.ModelViewSet):
    queryset = Pomodoro.objects.all()
    serializer_class = ListUsersSerializer

    def retrieve(self, request, *args, **kwargs):
        Pomodoro.objects.filter(user_id=kwargs['pk'], started__gte=timezone.now()).order_by('-started')
        return super(TeamStatusViewSet, self).retrieve(request, *args, **kwargs)

