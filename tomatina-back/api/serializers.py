from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from api.models import Pomodoro
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PomodoroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pomodoro
        fields = ('url','id', 'user_id', 'is_canceled')
        only_read = ('started')


class ListUsersSerializer(serializers.ListSerializer):

    def validate(self, attrs):
        return attrs


class UserStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
    started = serializers.DateTimeField()
    pomodoros = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        list_serializer_class = ListUsersSerializer
