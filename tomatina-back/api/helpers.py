from django.utils import timezone
from django.conf import settings


def get_status(pomodoros):
    if not pomodoros:
        return None

    now = timezone.now()
    if now <= (pomodoros[0].started + timezone.timedelta(seconds=settings.POMODORO_DURATION)):
        return 'WORKING'

    return 'NOT_WORKING'
